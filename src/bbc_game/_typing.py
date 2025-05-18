from __future__ import annotations

from typing import TypeAlias, Callable, Type
from bbc_game.shop import BaseShop
from bbc_game.point_earning import BasePointEarning

UpgradeFunctionType: TypeAlias = Callable[float, float]
PointEarningFunctionType: TypeAlias = Callable[float, float]
ShopType: TypeAlias = Type[BaseShop]
PointEarning: TypeAlias = BasePointEarning
