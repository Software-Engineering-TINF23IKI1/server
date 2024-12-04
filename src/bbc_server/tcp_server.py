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

# Variables to store the server and connected clients
global is_server_running, tcp_server, active_clients
is_server_running = True
tcp_server = None
active_clients = []

def stop_server(signum, frame):
    """This method is executed on Ctr-C. 
    It will shut down the server.

    Args:
        signum (_type_): value needed for Ctr-C interception
        frame (_type_): value needed for Ctr-C interception
    """
    print(">>> Stopping server...")
    global is_server_running
    is_server_running = False

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", PORT))

    connection_listener_thread.join()
    tcp_server.close()
    print(">>> Server sucesfully closed!")
    exit(1)


def connection_listener():
    """The listener accepting new connections to the server.
    """
    global is_server_running
    while is_server_running:
        (tcp_client, client_address) = tcp_server.accept()
        print(f">>> Handling new client from [{client_address}]")
        tcp_client.setblocking(False)
        active_clients.append((tcp_client, client_address))
        sleep(1)

if __name__ == "__main__":
    HOST = CONFIG.get("server", "HOST")
    PORT = int(CONFIG.get("server", "PORT").strip())

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((HOST, PORT))
    tcp_server.listen()
    signal(SIGINT, stop_server)

    connection_listener_thread = Thread(target = connection_listener)
    connection_listener_thread.start()

    while is_server_running:
        for tcp_client, client_address in active_clients:
            try:
                data = tcp_client.recv(1024).strip()
            except ConnectionResetError:
                active_clients.remove((tcp_client, client_address))
                print(f">>> Client [{client_address}] lost connection")
                continue # Error: Eine vorhandene Verbindung wurde vom Remotehost geschlossen
            except BlockingIOError:
                continue

            print(f"[{client_address}] {data.decode()}")
            # just send back the same data, but upper-cased
            tcp_client.sendall(data.upper())

        sleep(1)
