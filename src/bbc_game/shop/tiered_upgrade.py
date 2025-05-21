from __future__ import annotations
from typing import Optional
from bbc_game.shop.upgrade import Upgrade
from bbc_game.shop.single_upgrade import SingleUpgrade

class TieredUpgrade(Upgrade):
    """TieredUpgrade

    Args:
        upgrades (list[SingleUpgrade]): list of single upgrades that represents this tiered upgrade
        name (Optional[str], optional): name of the Tiered Upgrade. Defaults to None.
        description (Optional[str], optional): description of the tiered upgrade. Defaults to None.
    """

    def __init__(self, upgrades: list[SingleUpgrade], name: Optional[str] = None, description: Optional[str] = None):
        self._upgrades = upgrades
        self._current_tier = 0  # marker for the current tier (shows the next not yet purchased upgrade)
        self._max_tier = len(upgrades) - 1
        super().__init__(name, description)

    @property
    def upgrades(self) -> list[SingleUpgrade]:
        return self._upgrades

    @property
    def current_tier(self) -> int:
        """returns the current tier is"""
        return self._current_tier
    
    @property
    def max_tier(self) -> int:
        """returns the max tier"""
        return self._max_tier
    
    def current_upgrade(self) -> SingleUpgrade:
        """returns the SingleUpgrade object of the current tier (useful for displaying name, price etc.)"""
        return self._upgrades[self._current_tier]

    def upgrade(self):
        """upgrade to the next tier"""
        if not self._current_tier == self._max_tier:
            self._upgrades[self._current_tier].purchase()
            self._current_tier += 1

    def clone(self) -> TieredUpgrade:
        upgrades = [upgrade.clone() for upgrade in self._upgrades]
        return TieredUpgrade(upgrades=upgrades, name=self.name)



