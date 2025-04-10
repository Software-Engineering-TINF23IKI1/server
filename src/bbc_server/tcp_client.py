from socket import socket, AddressInfo

class Tcp_client:
    PACKET_SEPERATOR = '\x1E'

    def __init__(self, client: socket, address: AddressInfo):
        """Creates a Tcp_client object from a given tcp socket and connection address

        Args:
            client (socket): the socket used for this connection
            address (AddressInfo): the address of this connection
        """
        self._client = client
        self._client.setblocking(False)
        self.address = address

        self._text = ""
        self._package_queue = list()
        self._is_running = True

    def has_content(self) -> bool:
        """Returns whether or not data is available from the Tcp_client

        Returns:
            bool: True if content is available, False otherwise
        """
        if not self._is_running:
            return False

        if self._package_queue:
            return True

        try:
            while Tcp_client.PACKET_SEPERATOR not in self._text:
                data = self._client.recv(1024)
                self._text += data.decode()
        except ConnectionResetError:
            self._is_running = False
            print(f">>> client [{self.address}] lost connection")
            return False
        except BlockingIOError:
            return False

        packages = self._text.split(Tcp_client.PACKET_SEPERATOR)
        self._package_queue.extend(packages[:-1])
        self._text = packages[-1]

        return True

    def read_string(self) -> str | None:
        """Reads a string object from the Tcp_client

        Returns:
            str | None: Returns the string element if one can be read, None otherwise
        """
        if not self.has_content():
            return None

        return self._package_queue.pop(0)

    def send_string(self, content: str):
        """Sends a string object to the Tcp_client

        Args:
            content (str): The string object to send
        """
        if not self._is_running:
            return

        self._client.sendall((content + Tcp_client.PACKET_SEPERATOR).encode())
