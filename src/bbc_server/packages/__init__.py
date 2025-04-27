from bbc_server.packages.base import BasePackage
from bbc_server.packages.connect_to_game_session_package import ConnectToGameSessionPackage
from bbc_server.packages.end_routine_package import EndRoutinePackage
from bbc_server.packages.exception_package import ExceptionPackage, PackageParsingExceptionPackage, InvalidGameCodeExceptionPackage
from bbc_server.packages.game_start_package import GameStartPackage
from bbc_server.packages.game_update_package import GameUpdatePackage
from bbc_server.packages.lobby_status_package import LobbyStatusPackage
from bbc_server.packages.player_clicks_package import PlayerClicksPackage
from bbc_server.packages.start_game_session_package import StartGameSessionPackage
from bbc_server.packages.status_update_package import StatusUpdatePackage

# dictionairy to map package names to actual package classes
PACKAGE_DICT = {
    "connect-to-game-session": ConnectToGameSessionPackage,
    "end-routine": EndRoutinePackage,
    "exception": ExceptionPackage,
    "game-start": GameStartPackage,
    "game-update": GameUpdatePackage,
    "lobby-status": LobbyStatusPackage,
    "player-clicks": PlayerClicksPackage,
    "start-game-session": StartGameSessionPackage,
    "status-update": StatusUpdatePackage
}


from bbc_server.packages import decoder as Decoder