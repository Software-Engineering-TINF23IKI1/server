from bbc_server.packages import BasePackage

class EndRoutinePackage(BasePackage):
    PACKAGE_TYPE = "end-routine"

    def __init__(self, score: float, is_winner: bool, scoreboard: list[dict]):
        self.__score = score
        self.__is_winner = is_winner
        if not self.is_top_player_list_valid(scoreboard):
            raise ValueError("player list is not valid")
        self.__scoreboard = scoreboard

    def is_scoreboard_valid(self, scoreboard: list[dict]) -> bool:
        """check if the top player list is in the defined format
        This is done performing only structural checks.
        More information on the required strcture and data can be found in the package documentation

        Args:
            scoreboard (list[dict]): input player list

        Returns:
            bool: flag
        """
        keys = {"playername", "score"}
        keys_valid = all([set(player.keys()) == keys for player in scoreboard])
        return keys_valid

    def _generate_body_dict(self) -> dict:
        dict_repr = {
            "score": self.__score,
            "is-winner": self.__is_winner,
            "scoreboard": self.__scoreboard
        }
        return dict_repr

    @property
    def score(self) -> float:
        return self.__score

    @property
    def is_winner(self) -> bool:
        return self.__is_winner

    @property
    def scoreboard(self) -> list[dict]:
        return self.__scoreboard

