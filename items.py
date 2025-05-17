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

class ShopItem(Item):
    def __init__(self, item: Item, price: float):
        super().__init__(item.id, item.name, item.description)