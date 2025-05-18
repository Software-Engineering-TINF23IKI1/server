from __future__ import annotations

from typing import TypeAlias, Callable
from bbc_game.shop import BaseShop

UpgradeFunctionType: TypeAlias = Callable[float, float]
PointEarningFunctionType: TypeAlias = Callable[float, float]
ShopType: TypeAlias = BaseShop
