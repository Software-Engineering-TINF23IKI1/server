from game_status import Game_state
from game_code import generate_game_code, unregister_game_code

class Game_session:
    def __init__(self):
        self.code = generate_game_code()
        self.players = []
        self.state = Game_state.Preperation

        self.point_earn_system = None
        self.end_condition = None
        self.shop = None

    def cleanup(self):
        unregister_game_code(self.code)
