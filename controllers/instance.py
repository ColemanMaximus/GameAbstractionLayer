from abc import ABC, abstractmethod

from containers.registry import EntityRegistry
from models.map import Map, MapCell
from models.entity import NPC
from models.npc import NpcData


class Instance(ABC):
    def __init__(self, source):
        self.__source = source

    @property
    def source(self):
        return self.__source

    @abstractmethod
    def kill(self):
        pass


class MapCellInstance(Instance):
    def __init__(self, map_cell: MapCell):
        super().__init__(map_cell)
        self.__entities = EntityRegistry()

    @property
    def cell(self) -> MapCell:
        return self.source

    @property
    def entities(self) -> EntityRegistry:
        return self.__entities

    def init_entities(self):
        if not self.cell.entities:
            return

        for npcdata in self.cell.npcs:
            if not isinstance(npcdata, NpcData):
                continue

            self.entities.add(
                NPC(len(self.entities) + 1, npcdata)
            )

    def kill(self):
        pass


class MapInstance(Instance):
    def __init__(self, map: Map):
        super().__init__(map)
        self.__active_cell = None

        if map.map_cells:
            self.load_cell(map.map_cells[0])

    @property
    def map(self) -> Map:
        return self.source

    def load_cell(self, map_cell: MapCell | None):
        if not map_cell:
            return

        self.__active_cell = MapCellInstance(map_cell)

    @property
    def active_cell(self) -> MapCellInstance:
        return self.__active_cell

    def kill(self):
        pass