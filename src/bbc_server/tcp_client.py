import socket
from typing import Optional
from bbc_server._typing import BBCPackage
from bbc_server.packages import Decoder, PackageParsingExceptionPackage
from json import JSONDecodeError
from threading import Thread
import time
from bbc_server.exceptions import InvalidPackageTypeException, InvalidBodyException

class TcpClient:
    PACKET_SEPERATOR = '\x1E'

    def __init__(self, client: socket.socket, address: socket.AddressInfo):
        """Creates a Tcp_client object from a given tcp socket and connection address

        Args:
            client (socket): the socket used for this connection
            address (socket.AddressInfo): the address of this connection
        """
        self._client = client
        self._client.setblocking(False)
        self.address = address

        self._text = ""  # A storage to hold read but not yet parsed text from the client
        self._package_queue = list()
        self.is_running = True

        self._outgoing_queue = list()
        # Start a thread for sending packages to the client
        self.thread = Thread(target=self._send_message_thread)
        self.thread.start()

    def _send_message_thread(self):
        """Sends elements of the outgoing queue
        """
        while self.is_running:
            while self._outgoing_queue:
                try:
                    self._client.sendall((self._outgoing_queue.pop(0) + TcpClient.PACKET_SEPERATOR).encode())
                except (ConnectionResetError, ConnectionAbortedError):
                    print(f">>> client [{self.address}] lost connection")
                    self.is_running = False
                    return

            time.sleep(0.1)

    def has_content(self) -> bool:
        """Returns whether or not data is available from the Tcp_client

        Returns:
            bool: True if content is available, False otherwise
        """
        if not self.is_running:
            return False

        if self._package_queue:
            return True

        try:
            while TcpClient.PACKET_SEPERATOR not in self._text:
                data = self._client.recv(1024)
                if not data:
                    raise ConnectionAbortedError()
                self._text += data.decode()
        except (ConnectionResetError, ConnectionAbortedError):
            self.is_running = False
            print(f">>> client [{self.address}] lost connection")
            return False
        except BlockingIOError:
            return False

        packages = self._text.split(TcpClient.PACKET_SEPERATOR)
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
        if not self.is_running:
            return

        self._outgoing_queue.append(content)

    def read_package(self, **kwargs) -> Optional[BBCPackage]:
        """read a package if available
        If a package is invalid the next package is automatically read.

        Returns:
            Optional[BBCPackage]: input package
        """
        while self.has_content():
            try:
                return Decoder.deserialize(self.read_string())
            except JSONDecodeError as e:
                details = {
                    "raw_msg": str(e)
                }
                self.send_package(PackageParsingExceptionPackage(stage="JSON", details=details))
            except InvalidPackageTypeException as e:
                details = {
                    "raw_msg": str(e)
                }
                self.send_package(PackageParsingExceptionPackage(stage="Package-Type", details=details))
            except InvalidBodyException as e:
                details = {
                    "raw_msg": str(e)
                }
                self.send_package(PackageParsingExceptionPackage(stage="Body", details=details))


    def send_package(self, package: BBCPackage, **kwargs) -> None:
        """send package to the Client

        Args:
            package (BBCPackage): package to send
        """
        self.send_string(package.to_json())
