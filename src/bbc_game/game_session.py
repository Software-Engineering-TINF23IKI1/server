from bbc_game.game_state import GameState
from bbc_game.game_code import generate_game_code, unregister_game_code
from bbc_server.packages import LobbyStatusPackage
from threading import Thread
from bbc_server import Player
import time

class GameSession:
    def __init__(self):
        """Generates a new empty game session with a newly generated game code
        """
        self.code = generate_game_code()
        self.players: list[Player]
        self.players = []
        self.state = GameState.Preperation

        self.point_earn_system = None
        self.end_condition = None
        self.shop = None

        # Start the game lobby loop
        self.thread = Thread(target=self.lobby_loop)
        self.thread.start()

    def lobby_loop(self):
        loop_iteration = 0
        while self.state is GameState.Preperation:

            # Writing Dict with if Players are ready
            self.readyStatus: list[dict[Player, bool]] = {}        
            #for player in self.players:
            #    self.readyStatus[player] = player.is_ready
            for player in self.players:
                self.ready_status.append({"playername": player.name, "is-ready": player.is_ready})

            allPlayersReady = all(player["ready"] for player in self.ready_status)

            # Send lobby status package

            for player in self.players:
                player.send_package(LobbyStatusPackage(self.code,self.readyStatus))
            
            
            # Icrease iterator if all Players are ready
            if allPlayersReady:
                loop_iteration += 1

            if not allPlayersReady:
                loop_iteration = 0 # Reset Loop Iteration Counter so waiting for all players restarts

            if allPlayersReady and loop_iteration >= 400:
                # End Lobby loop and go over into Game Loop
                pass

            time.sleep(0.1)

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
