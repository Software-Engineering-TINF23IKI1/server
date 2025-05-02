from __future__ import annotations

import socket
import sys
import pathlib
from typing import Any, Callable
import typing
import os
import time
from typing import Optional
from json import JSONDecodeError
from threading import Thread
import types
import ast
import signal



BBC_SERVER_DIR = pathlib.Path(__file__).parent.parent / "src"

sys.path.insert(0, os.path.join(BBC_SERVER_DIR))
sys.path.insert(0, os.path.join(pathlib.Path(__file__).parent.parent))

import bbc_server
from bbc_server.exceptions import InvalidPackageTypeException, InvalidBodyException
from bbc_server.packages import Decoder, PackageParsingExceptionPackage
from bbc_server._typing import BBCPackage


class TcpTestClient:
    PACKET_SEPERATOR = '\x1E'

    def __init__(self, ip: str, port: int):
        """Creates a Tcp_client object from a given tcp socket

        Args:
            client (socket): the socket used for this connection
        """
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((ip, port))
        self._client.setblocking(False)

        self._text = ""  # A storage to hold read but not yet parsed text from the client
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
            while self.PACKET_SEPERATOR not in self._text:
                data = self._client.recv(1024)
                if not data:
                    raise ConnectionAbortedError()
                self._text += data.decode()
        except (ConnectionResetError, ConnectionAbortedError):
            self._is_running = False
            print(f">>> client lost connection")
            return False
        except BlockingIOError:
            return False

        packages = self._text.split(self.PACKET_SEPERATOR)
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

        try:
            self._client.sendall((content + self.PACKET_SEPERATOR).encode())
        except (ConnectionResetError, ConnectionAbortedError):
            print(f">>> client lost connection")
            self._is_running = False

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

    def shutdown(self):
        self._is_running = False
        self._client.shutdown()


class InterActiveTestClient(TcpTestClient):

    def __init__(self, ip, port, listener_delay: float = 0.5, filter_function: Optional[Callable] = None):
        super().__init__(ip, port)
        self.listener_delay = listener_delay
        self.filter_function = filter_function

    def make_interactive(self):
        signal.signal(signal.SIGINT, self._stop)
        self._listener_thread = Thread(target=self._listen_to_packages)
        self._listener_thread.start()
        self._package_input_loop()

    def _listen_to_packages(self):
        while self._is_running:
            pkg = self.read_package()
            if pkg:
                if self.filter_function:
                    pkg = self.filter_function(pkg)
                if pkg:
                    print(pkg)
            time.sleep(self.listener_delay)

    def _generate_pkg_string(self):
        package_str = "raw string input [-1]; "
        packages = bbc_server.packages.PACKAGE_DICT
        for idx, package in enumerate(packages.keys()):
            package_str += f"{package} [{idx}]; "
        return package_str

    def _package_input_loop(self):
        packages = bbc_server.packages.PACKAGE_DICT
        while True:
            print("Please select from the list of packages:")
            print(self._generate_pkg_string())
            selection = int(input("Type number to select: "))
            if selection == -1:
                self.send_string(input("raw string input: "))
                continue
            package_class = list(packages.values())[selection]
            cls_parameters = {}
            hints = typing.get_type_hints(package_class.__init__)

            for key, parameter in package_class.JSON_PARAM_MAP.items():
                param_type = hints[parameter]
                if isinstance(param_type, types.GenericAlias) and "dict" in str(param_type):
                    # handle dict inputs
                    cls_parameters[parameter] = dict(ast.literal_eval(input(f"{key} (as raw dict): ")))
                else:
                    param_in = input(f"{key}: ")
                    cls_parameters[parameter] = self._cast_objects(param_in, param_type)

            # create package
            package = package_class(**cls_parameters)
            self.send_package(package)

    def _stop(self, signum, frame):
        self._is_running = False
        self._listener_thread.join()

    def _cast_objects(self, value: str, target_type: Any):
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == bool:
            return bool(value)
        elif target_type == str:
            return value


def main():
    from tests import TEST_CONFIG

    IP = str(TEST_CONFIG.get("test_server", "IP")).strip()
    PORT = int(TEST_CONFIG.get("test_server", "PORT").strip())
    client = InterActiveTestClient(IP, PORT)
    client.make_interactive()


if __name__ == "__main__":
    main()
