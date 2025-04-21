from bbc_server.tcp_client import TcpClient
from bbc_game.game_session import GameSession
from bbc_game.game_state import GameState
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
        print(f">>> Server listening on [{host or "localhost"}:{port}]")

        signal.signal(signal.SIGINT, self.stop_server)

        self.players = []
        self.game_sessions = {}

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

                if False:  # Creates a new game session and adds the current player to the session
                    session = self.create_game_session()
                    session.add_player(player)
                    self.players.remove(player)

                package = player.read_string()
                print(f"[{player.address}] {package}")
                player.send_string(package.upper())

            time.sleep(0.2)

    def stop_server(self, signum, frame):
        """Stops the Tcp_server and the running threads on Ctrl-C

        Args:
            signum : Value needed for Ctrl-C interception
            frame : Value needed for Ctrl-C interception
        """
        print(">>> Stopping server...")

        self._is_server_running = False

        for session in self.game_sessions.values():
            session.state = GameState.Kill
            session.thread.join()

        # Stop package listener
        self._package_listener_thread.join()

        # Close server
        self._server.close()

        print(">>> Server sucessfully closed!")

    def create_game_session(self) -> GameSession:
        """Creates a new game session and adds it to the game session dictionary

        Returns:
            GameSession: The newly created game session
        """
        session = GameSession()
        self.game_sessions[session.code] = session
        return session


if __name__ == "__main__":
    from bbc_server import CONFIG
    host = CONFIG.get("server", "HOST")
    port = int(CONFIG.get("server", "PORT").strip() or "0")

    TcpServer(host, port)
