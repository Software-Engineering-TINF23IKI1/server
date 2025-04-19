from bbc_server.packages import BasePackage

class GameUpdatePackage(BasePackage):
    PACKAGE_TYPE = "game-update"

    N_TOP_PLAYERS = 5  # amount of players to show in the leaderboard

    def __init__(self, currency: float, score: float, top_players: list[dict]):
        """GameUpdatePackage
        see the package documentation for more information

        Args:
            currency (float): currency of the player
            score (float): score of the player
            top_players (list[dict]): list of top N players with their respective scores
        """
        self.__currency = currency
        self.__score = score
        if not self.is_top_player_list_valid(top_players):
            raise ValueError("player list is not valid")
        self.__top_players = top_players

    def is_top_player_list_valid(self, players: list[dict]) -> bool:
        """check if the top player list is in the defined format
        This is done performing only structural checks.
        More information on the required strcture and data can be found in the package documentation

        Args:
            players (list[dict]): input player list

        Returns:
            bool: flag
        """
        keys = {"playername", "score"}
        keys_valid = all(set(player.keys()) == keys for player in players)
        length_valid = (len(players) <= self.N_TOP_PLAYERS)
        return keys_valid and length_valid

    def _generate_body_dict(self) -> dict:
        dict_repr = {
            "currency": self.__currency,
            "score": self.__score,
            "top-players": self.__top_players
        }
        return dict_repr

    @property
    def currency(self) -> float:
        return self.__currency

    @property
    def score(self) -> float:
        return self.__score

    @property
    def top_players(self) -> list[dict]:
        return self.__top_players

