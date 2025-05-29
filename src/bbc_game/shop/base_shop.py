from abc import ABC
from bbc_game.shop.upgrade import Upgrade

class BaseShop(ABC):
    """Base Class for custom Shops

    ClassVars:
    - shop_entries: dictionairy holding the different upgrades

    """
    shop_entries: list[Upgrade] = None

    def __init__(self):
        if not self.shop_entries:
            raise NotImplementedError("Shops must provide the shop_entries classvar")
        
        self._upgrades = {upgrade.name: upgrade.clone() for upgrade in self.shop_entries}

    @property
    def upgrades(self) -> dict[str, Upgrade]:
        return self._upgrades

