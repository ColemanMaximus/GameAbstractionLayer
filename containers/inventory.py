from abc import ABC

from containers.registry import Registry
from models.items import Item


class Inventory(Registry, ABC):
    def __init__(self, items: Registry = None):
        super().__init__()
        if items:
            self.__add_regitems(items)

    @property
    def items(self):
        return self._items

    def __add_regitems(self, items: Registry):
        for item in items:
            self.add(item)


class InventoryItem(Item):
    def __init__(self,
                 inv_id,
                 inventory: Inventory,
                 item: Item,
                 obtained_ts: float = None
                 ):
        self.__inventory = inventory
        self.__inv_id = inv_id
        self.__obtained = obtained_ts
        super().__init__(item.id, item.name, item.description)

    @property
    def inv_id(self):
        return self.__inv_id

    @property
    def inventory(self):
        return self.__inventory

    @property
    def obtained(self):
        return self.__obtained


class PlayerInventory(Inventory):
    def __init__(self, character, items: Registry = None):
        self.__character = character
        super().__init__(items)

    @property
    def character(self):
        return self.__character


class ShopInventory(Inventory):
    def __init__(self, items: Registry = None):
        super().__init__(items)
