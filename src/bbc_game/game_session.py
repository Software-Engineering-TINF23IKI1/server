from bbc_game.game_state import GameState
from bbc_game.game_code import generate_game_code, unregister_game_code
from threading import Thread
from bbc_server import Player
import time

class GameSession:
    def __init__(self):
        """Generates a new empty game session with a newly generated game code
        """
        self.code = generate_game_code()
        self.players = []
        self.state = GameState.Preperation

        self.point_earn_system = None
        self.end_condition = None
        self.shop = None

        # Start the game lobby loop
        self.thread = Thread(target=self.lobby_loop)
        self.thread.start()

    def lobby_loop(self):
        while self.state is GameState.Preperation:
            allPlayersReady = all(player.isReady() for player in self.players)

            pass  # Send lobby status package

            time.sleep(0.1) # Needs to be revisited 

    def add_player(self, player: Player) -> bool:
        """Adds a player to the game session scope. When a player enters the game session scope, player packets will
        be managed by the game session directly. Players can only be added to the scope, while the session is in the
        preperation state.

        Args:
            player (Player): the player to add to the game session scope

        Returns:
            bool: whether the player could be added to the game session scope
        """
        if self.state != GameState.Preperation:
            return False

        print(f">>> {player.name or 'Player'} [{player.client.address}] joined Session [{self.code}]")
        self.players.append(player)
        return True

    def cleanup(self):
        """Cleans all resources used by the game session directly
        """
        unregister_game_code(self.code)
