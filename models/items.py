from containers.inventory import InventoryItem
from models.currency import Currency


class Item:
    def __init__(self, id, name, description = ""):
        self.__id = id
        self.name = name
        self.description = description

    @property
    def id(self):
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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