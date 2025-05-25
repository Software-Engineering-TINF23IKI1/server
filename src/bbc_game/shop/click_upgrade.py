from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from bbc_game.shop.single_upgrade import SingleUpgrade
if TYPE_CHECKING:
    from bbc_game._typing import UpgradeFunctionType

class ClickUpgrade(SingleUpgrade):
    """class for the Click modifier upgrade

    Args:
        price (float): price of the upgrade
        upgrade_function (UpgradeFunctionType): function mapping the current modifier to the new modifier
        name (Optional[str], optional): name of the upgrade. Defaults to None.
        description (Optional[str], optional): description of the upgrade. Defaults to None.
    """

    def __init__(self, price: float, upgrade_function: UpgradeFunctionType, name: Optional[str]= None, description: Optional[str] = None):
        self._upgrade_function = upgrade_function
        super().__init__(price, name, description)

    @property
    def upgrade_function(self) -> UpgradeFunctionType:
        return self._upgrade_function
    
    def apply_upgrade(self, current_modifier: float) -> float:
        """wrapper funciton that calculates the new click modifier after 'applying' the upgrade

        Args:
            current_modifier (float): current click modifier

        Returns:
            float: the new modifier
        """
        return self._upgrade_function(current_modifier)
    
    def clone(self) -> ClickUpgrade:
        return ClickUpgrade(price=self._price, upgrade_function=self._upgrade_function, name=self.name)
