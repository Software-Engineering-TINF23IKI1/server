from bbc_game.game_config import BaseGame
from bbc_game.configs.default.default_shop import DefaultShop

default_game = BaseGame(shop=DefaultShop, base_currency=0, base_earn_rate=0, base_modifier=1)
