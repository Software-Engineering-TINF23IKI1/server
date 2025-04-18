from bbc_server.packages import BasePackage

class ConnectToGameSessionPackage(BasePackage):
    PACKAGE_TYPE = "connect-to-game-session"

    def __init__(self, gamecode: str, playername: str):
        self.__gamecode = gamecode
        self.__playername = playername

    def _generate_body_dict(self) -> dict:
        dict_repr = {
            "gamecode": self.__gamecode,
            "playername": self.__playername
            }
        return dict_repr

    @property
    def gamecode(self) -> str:
        return self.__gamecode

    @property
    def playername(self) -> str:
        return self.__playername
    
