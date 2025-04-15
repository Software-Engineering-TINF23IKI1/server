from game_status import Game_state

class Game_session:
    def __init__(self):
        self.code = None
        self.players = None
        self.state = Game_state.Preperation

        self.point_earn_system = None
        self.end_condition = None
        self.shop = None

        pass
