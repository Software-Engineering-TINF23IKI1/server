from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from bbc_server.tcp_client import TcpClient

from bbc_server._typing import BBCPackage

class Player:
    def __init__(self, client: TcpClient, name: str = None, is_ready: bool = False, currency: float = 0, earn_rate: float = 0):
        """class representing an individual player

        Args:
            client (TcpClient): the TCP Client used
            name (str, optional): player name. Defaults to None.
            is_ready (bool, optional): readiness status. Defaults to False.
            currency (float, optional): currency. Defaults to 0.
            earn_rate (float, optional): earn_rate. Defaults to 0.
        """
        self._client = client
        self._name = name
        self._is_ready = is_ready
        self._currency = currency
        self._points = 0
        self._earn_rate = earn_rate

    @property
    def client(self) -> TcpClient:
        return self._client

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def is_ready(self) -> bool:
        return self._is_ready

    @is_ready.setter
    def is_ready(self, is_ready: bool) -> None:
        self._is_ready = is_ready

    @property
    def currency(self) -> float:
        return self._currency

    @currency.setter
    def currency(self, currency: float) -> None:
        self._currency = currency

    @property
    def points(self) -> float:
        return self._points

    @points.setter
    def points(self, points: float) -> None:
        self._points = points

    @property
    def earn_rate(self) -> float:
        return self._earn_rate

    @earn_rate.setter
    def earn_rate(self, earn_rate: float) -> float:
        self._earn_rate = earn_rate

    def read_package(self, **kwargs) -> Optional[BBCPackage]:
        """read a package if available (wraps TCPClient.read_package())
        If a package is invalid the next package is automatically read.

        Returns:
            Optional[BBCPackage]: input package
        """
        return self._client.read_package(**kwargs)

    def send_package(self, package: BBCPackage, **kwargs) -> None:
        """send package to the Client (wraps TCPClient.send_package())

        Args:
            package (BBCPackage): package to send
        """
        self._client.send_package(package=package, **kwargs)

