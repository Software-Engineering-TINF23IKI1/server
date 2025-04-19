from bbc_server.packages import BasePackage

class PlayerClicksPackage(BasePackage):
    PACKAGE_TYPE = "player-clicks"

    def __init__(self, count: int):
        """PlayerClicksPackage
        see the package documentation for more information

        Args:
            count (int): raw click count
        """
        self.__count = count

    def _generate_body_dict(self) -> dict:
        return {"count": self.__count}

    @property
    def count(self) -> int:
        return self.__count

