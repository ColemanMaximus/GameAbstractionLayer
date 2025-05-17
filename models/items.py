from containers.inventory import Inventory

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

    def __str__(self):
        return self.name


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
