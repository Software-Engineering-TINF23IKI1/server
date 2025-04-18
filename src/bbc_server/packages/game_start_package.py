from bbc_server.packages import BasePackage

class GameStartPackage(BasePackage):
    PACKAGE_TYPE = "game-start"

    def __init__(self):
        pass

    def _generate_body_dict(self) -> dict:
        return {}


