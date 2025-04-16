from bbc_game.game_state import GameState
from bbc_game.game_code import generate_game_code, unregister_game_code

class Game_session:
    def __init__(self):
        """Generates a new empty game session with a newly generated game code
        """
        self.code = generate_game_code()
        self.players = []
        self.state = GameState.Preperation

        self.point_earn_system = None
        self.end_condition = None
        self.shop = None

    def add_player(self, player) -> bool:
        """Adds a player to the game session scope. When a player enters the game session scope, player packets will
        be managed by the game session directly. Players can only be added to the scope, while the session is in the
        preperation state.

        Args:
            player (_type_): the player to add to the game session scope

        Returns:
            bool: whether the player could be added to the game session scope
        """
        if self.state != GameState.Preperation:
            return False

        self.players.append(player)
        return True

    def cleanup(self):
        """Cleans all resources used by the game session directly
        """
        unregister_game_code(self.code)
