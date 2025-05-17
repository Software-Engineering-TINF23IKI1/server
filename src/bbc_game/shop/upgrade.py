from typing import Optional
from abc import ABC, abstractmethod

class Upgrade(ABC):
    """base class for upgrades

    Args:
        name (Optional[str], optional): name of the upgrade. Defaults to None.
        description (Optional[str], optional): description of the upgrade. Defaults to None.
    """

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None):
        self.name = name
        self.description = description

    @abstractmethod
    def clone(self):
        """method cloning the Upgrade"""
        pass
