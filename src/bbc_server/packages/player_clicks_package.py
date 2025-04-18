from bbc_server.packages import BasePackage

class PlayerClicksPackage(BasePackage):
    PACKAGE_TYPE = "player-clicks"

    def __init__(self, count: int):
        self.__count = count

    def _generate_body_dict(self) -> dict:
        return {"count": self.__count}

    @property
    def count(self) -> int:
        return self.__count

