from bbc_server.tcp_client import TcpClient
from threading import Thread
import time
import signal
import socket

class TcpServer:
    def __init__(self, host: str, port: int):
        """Creates and starts a Tcp_server on the provided host and port

        Args:
            host (str): the host submask to start the server on (To allow global traffic, use '0.0.0.0')
            port (int): the port the server listens on
        """
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((host, port))
        self._server.listen()
        self._server.setblocking(False)

        self._is_server_running = True
        print(f">>> Server listening on [{host}:{port}]")

        signal.signal(signal.SIGINT, self.stop_server)

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
                self.players.append(TcpClient(client, address))
            except BlockingIOError:
                time.sleep(1)

    def _package_listener(self):
        """Loop listening for packages on the players currently assigned to the Tcp_server
        """
        while self._is_server_running:
            for player in self.players:
                if not player.has_content():
                    continue

                package = player.read_package()

                # package = player.read_string()
                if package:
                    print(f"[{player.address}] {package.to_json()}")
                    player.send_string("confirmation")

            time.sleep(0.2)

    def stop_server(self, signum, frame):
        """Stops the Tcp_server and the running threads on Ctrl-C

        Args:
            signum : Value needed for Ctrl-C interception
            frame : Value needed for Ctrl-C interception
        """
        print(">>> Stopping server...")
        for player in self.players:
            player.send_string("server is shutting down.")

        self._is_server_running = False

        self._package_listener_thread.join()
        self._server.close()

        print(">>> Server sucessfully closed!")


if __name__ == "__main__":
    from bbc_server import CONFIG
    host = CONFIG.get("server", "HOST")
    port = int(CONFIG.get("server", "PORT").strip() or "0")

    TcpServer(host, port)
