class Registry:
    def __init__(self):
        self.__items = []

    @property
    def _items(self):
        return iter(self.__items)

    @_items.setter
    def _items(self, items):
        self.__items = items

    def add(self, item):
        self.__items.append(item)

    def delete(self, item):
        self.__items.remove(item)

    def __iter__(self):
        return self.__items

class AccountRegistry(Registry):
    def __init__(self):
       super().__init__()

    @property
    def accounts(self):
        return self._items

    def __iter__(self):
        return self._items

class CharacterRegistry(Registry):
    def __init__(self):
       super().__init__()

    @property
    def characters(self):
        return self._items

    def __iter__(self):
        return self._items