class NpcData:
    def __init__(self, npc_id, name: str):
        self.__npc_id = npc_id
        self.name = name

    @property
    def npc_id(self):
        return self.__npc_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name