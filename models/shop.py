from containers.inventory import Inventory
from containers.interface import Interface
from models.items import InventoryItem
from models.currency import Currency

class ShopInventory(Inventory):
    def __init__(self, *items):
        super().__init__(items)


class ShopItem(InventoryItem):
    def __init__(self, item: InventoryItem, currency: Currency = None, price: int | float = 0):
        if not isinstance(item, InventoryItem):
            raise ValueError("ShopItems can only be instantiated with InventoryItem objects.")

        super().__init__(item.inv_id, item.inventory, item, item.obtained)
        self.currency = currency
        self.price = price

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency: Currency):
        if not isinstance(currency, Currency):
            raise ValueError("Object isn't an instance of a currency.")

        self.__currency = currency

    @property
    def price(self) -> int | float:
        return self.__price

    @price.setter
    def price(self, price: int | float):
        if price < 0:
            raise ValueError("Unsupported negative values in item price.")

        self.__price = price

class Shop(Interface):
    def __init__(self, id, name: str, shop_inventory: ShopInventory = None):
        super().__init__(name)
        self.__id = id
        self.__shop_inventory = shop_inventory if shop_inventory else ShopInventory()

    @property
    def id(self):
        return self.__id

    @property
    def inventory(self) -> ShopInventory:
        return self.__shop_inventory

    @property
    def items(self):
        return iter(self.inventory.items)
