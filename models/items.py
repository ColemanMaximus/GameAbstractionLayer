class Item:
    def __init__(self, id, name: str, description: str, level: int, sprite: str):
        self.__id = id
        self.name = name
        self.description = description
        self.level = level
        self.__sprite = sprite

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

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        if level < 1:
            self.__level = 1

        self.__level = level

    @property
    def sprite(self) -> str:
        return self.__sprite

    def __str__(self):
        return self.name


class InventoryItem(Item):
    def __init__(self,
                 inv_id,
                 item: Item,
                 obtained_ts: float = None
                 ):
        self.__inv_id = inv_id
        self.__obtained = obtained_ts
        super().__init__(*[value for value in item.__dict__.values()])

    @property
    def inv_id(self):
        return self.__inv_id

    @property
    def obtained(self):
        return self.__obtained
