from bbc_server.packages import BasePackage

class GameStartPackage(BasePackage):
    PACKAGE_TYPE = "game-start"

    def __init__(self):
        """GameStartPackage
        see the package documentation for more information
        """
        pass

    def _generate_body_dict(self) -> dict:
        return {}


