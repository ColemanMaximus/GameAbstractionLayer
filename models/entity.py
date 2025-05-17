class Entity:
    def __init__(self, id, name: str, etype = None):
        self.__id = id
        self.name = name
        self.type = etype

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, etype):
        self.__type = etype

class Player(Entity):
    def __init__(self, char_id, name: str):
        super().__init__(char_id, name)

class NPC(Entity):
    def __init__(self, npc_id, name: str):
        super().__init__(npc_id, name)