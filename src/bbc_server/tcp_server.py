from threading import Thread
from time import sleep
import socket
from signal import signal, SIGINT

import os
import pathlib
import sys

here = pathlib.Path(__file__).parent
repo_root_dir = here.parent

sys.path.insert(0, os.path.join(repo_root_dir / "src" / "bbc_server"))
sys.path.insert(0, os.path.join(repo_root_dir))

from bbc_server import CONFIG

class Tcp_server:
    def __init__(self, HOST : str, PORT : int):
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.bind((HOST, PORT))
        self.tcp_server.listen()
        self.tcp_server.setblocking(False)

        self.is_server_running = True
        self.active_clients = []
        print(f">>> Server listening on port [{PORT}]")

        # Add Ctl-C Handler
        signal(SIGINT, self.stop_server)

        # Start connection listener
        self.connection_listener_thread = Thread(target = self.connection_listener)
        self.connection_listener_thread.start()

        self.server_listener()
    
    def server_listener(self):
        # Main client read loop
        while self.is_server_running:
            for tcp_client, client_address in self.active_clients:
                try:
                    # Read data from client
                    data = tcp_client.recv(1024).strip()
                    if not data: raise ConnectionResetError()
                except ConnectionResetError: # Client disconnected
                    self.active_clients.remove((tcp_client, client_address))
                    print(f">>> Client [{client_address}] lost connection")
                    continue
                except BlockingIOError: # No data available
                    continue

                # Handle data
                print(f"[{client_address}] {data.decode()}")
                # just send back the same data, but upper-cased
                tcp_client.sendall(data.upper())

            sleep(1)

    def connection_listener(self):
        """The listener accepting new connections to the server.
        """
        while self.is_server_running:
            try:
                (tcp_client, client_address) = self.tcp_server.accept()
                print(f">>> Handling new client from [{client_address}]")
                tcp_client.setblocking(False)
                self.active_clients.append((tcp_client, client_address))
            except BlockingIOError: # No new client available
                sleep(1)

    def stop_server(self, signum, frame):
        """This method is executed on Ctr-C. 
        It will shut down the server.

        Args:
            signum: value needed for Ctr-C interception
            frame: value needed for Ctr-C interception
        """
        print(">>> Stopping server...")
        # Sets running server variable to false
        self.is_server_running = False

        # Stop all running server processes
        self.connection_listener_thread.join()
        self.tcp_server.close()
        print(">>> Server sucesfully closed!")

if __name__ == "__main__":
    HOST = CONFIG.get("server", "HOST")
    PORT = int(CONFIG.get("server", "PORT").strip())

    Tcp_server(HOST, PORT)