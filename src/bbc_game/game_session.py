from bbc_game.game_state import GameState
from bbc_game.game_code import generate_game_code, unregister_game_code
import bbc_server._typing
import bbc_server.packages
from threading import Thread
from bbc_server import Player
from bbc_server._typing import BBCPackage
import bbc_server
import time

import bbc_server.exceptions
import bbc_server.packages
import bbc_server.packages.status_update_package

class GameSession:
    def __init__(self):
        """Generates a new empty game session with a newly generated game code
        """
        self.code = generate_game_code()
        self.players: list[Player] = []
        self.state = GameState.Preperation

        self.point_earn_system = None
        self.end_condition = None
        self.shop = None

        # Start the game lobby loop
        self.thread = Thread(target=self.lobby_loop)
        self.thread.start()

    def update_player_list(self):
        self.players = [player for player in self.players if player.client.is_running]

    def lobby_loop(self):
        loop_iteration = 0
        while self.state is GameState.Preperation:
            self.update_player_list()

            # Receiving Player Ready State
            for player in self.players:
                while received_package := player.read_package():
                    match received_package:
                        case bbc_server.packages.StatusUpdatePackage():
                            player.is_ready = received_package.is_ready
                        case _:
                            pass  # Logging
                
            
            
            # Sending Lobby Status
            player_list = [{"playername": inner_player.name, "is-ready": inner_player.is_ready} for inner_player in self.players]
            for player in self.players:
                player.send_package(
                    bbc_server.packages.LobbyStatusPackage(
                        self.code,
                        players=player_list
                        )
                )


            all_players_ready = all(player["is-ready"] for player in player_list)
            # Icrease iterator if all Players are ready
            if all_players_ready:
                loop_iteration += 1

            if not all_players_ready:
                loop_iteration = 0  # Reset Loop Iteration Counter so waiting for all players restarts

            if all_players_ready and loop_iteration >= 400:
                self.state = GameState.Running


            time.sleep(0.1)

        if self.state == GameState.Running:
            # Send Game Starting Package to players

            for player in self.players:
                player.send_package(
                    bbc_server.packages.GameStartPackage()
                )
            self.game_loop()


    def game_loop(self):
        while self.state is GameState.Running:
            # Game Loop
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

        for player in self.players:
            player.client.shutdown()
