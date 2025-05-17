from abc import ABC

from registry import Registry
from items import Item

class Inventory(Registry, ABC):
    def __init__(self):
        super().__init__()

    @property
    def items(self):
        return self._items

class InventoryItem(Item):
    def __init__(self, inventory: Inventory, id, name: str, description: str = ""):
        self.inventory = inventory
        super().__init__(id, name, description)

class PlayerInventory(Inventory):
    def __init__(self, character):
        self.__character = character
        super().__init__()

    @property
    def character(self):
        return self.__character