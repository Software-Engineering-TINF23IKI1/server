from bbc_server.packages import BasePackage

class StartGameSessionPackage(BasePackage):
    PACKAGE_TYPE = "start-game-session"

    def __init__(self, playername: str):
        self.__playername = playername

    def _generate_body_dict(self) -> dict:
        return {"playername": self.__playername}

    @property
    def playername(self) -> str:
        return self.__playername
    
