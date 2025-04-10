from tcp_client import Tcp_client
from signal import signal, SIGINT
from socket import socket
from time import sleep
from threading import Thread

# Evil python module hack
from pathlib import Path
from sys import path as sys_path
from os import path as os_path
here = Path(__file__).parent
repo_root_dir = here.parent
sys_path.insert(0, os_path.join(repo_root_dir / "src" / "bbc_server"))
sys_path.insert(0, os_path.join(repo_root_dir))

class Tcp_server:
    def __init__(self, host: str, port: int):
        """Creates and starts a Tcp_server on the provided host and port

        Args:
            host (str): the host submask to start the server on (To allow global traffic, use '0.0.0.0')
            port (int): the port the server listens on
        """
        self._server = socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((host, port))
        self._server.listen()
        self._server.setblocking(False)

        self._is_server_running = True
        print(f">>> Server listening on [{host}:{port}]")

        signal(SIGINT, self.stop_server)

        self.players = []

        self._package_listener_thread = Thread(target=self._package_listener)
        self._package_listener_thread.start()

        self._connection_listener()

    def _connection_listener(self):
        """Loop listening for new client connections
        """
        while self._is_server_running:
            try:
                (client, address) = self._server.accept()
                print(f">>> Handling new client from [{address}]")
                self.players.append(Tcp_client(client, address))
            except BlockingIOError:
                sleep(1)

    def _package_listener(self):
        """Loop listening for packages on the players currently assigned to the Tcp_server
        """
        while self._is_server_running:
            for player in self.players:
                if not player.has_content():
                    continue

                package = player.read_string()
                print(f"[{player.address}] {package}")
                player.send_string(package.upper())

            sleep(0.2)

    def stop_server(self, signum, frame):
        """Stops the Tcp_server and the running threads on Ctrl-C

        Args:
            signum : Value needed for Ctrl-C interception
            frame : Value needed for Ctrl-C interception
        """
        print(">>> Stopping server...")

        self.is_server_running = False

        self._package_listener_thread.join()
        self._server.close()

        print(">>> Server sucessfully closed!")


if __name__ == "__main__":
    from bbc_server import CONFIG
    host = CONFIG.get("server", "HOST")
    port = int(CONFIG.get("server", "PORT").strip() or "0")

    Tcp_server(host, port)
