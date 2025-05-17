from containers.registry import Registry


class MapRegistry(Registry):
    def __init__(self):
        super().__init__()


class MapCellRegistry(Registry):
    def __init__(self):
        super().__init__()

    @property
    def cells(self) -> iter:
        return iter(self._items)


class Map:
    def __init__(self, id, name: str, map_cells = MapCellRegistry):
        self.__id = id
        self.name = name
        self.__map_cells = map_cells

    @property
    def map_cells(self) -> iter:
        return self.__map_cells.cells

    def get_cell(self, id):
        for cell in self.map_cells:
            if cell.id == id:
                return cell

        return None


class MapCell:
    def __init__(self, map: Map, cell_name: str, cell_index: int):
        self.__map = map
        self.__cell_name = cell_name
        self.__cell_index = cell_index

    @property
    def map(self) -> Map:
        return self.__map

    @property
    def cell_name(self) -> str:
        return self.__cell_name

    @property
    def cell_index(self) -> int:
        return self.cell_index
