from typing import Optional
from bbc_game.shop.upgrade import Upgrade

class SingleUpgrade(Upgrade):
    """base class for individual upgrades

    Args:
        price (float): price of the upgrade
        name (Optional[str], optional): name of the upgrade. Defaults to None.
        description (Optional[str], optional): description of the upgrade. Defaults to None.
    """

    def __init__(self, price: float, name: Optional[str]= None, description: Optional[str] = None):
        self._price = price
        self._purchased = False
        super().__init__(name, description)

    @property
    def price(self) -> float:
        return self._price

    def purchase(self):
        """'purchase' the upgrade. This marks it as purchased."""
        self._purchased = True