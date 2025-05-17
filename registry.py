class Registry:
    def __init__(self):
        self.__items = []

    @property
    def _items(self):
        return self.__items

    @_items.setter
    def _items(self, items):
        self.__items = items

    def add(self, item):
        self.__items.append(item)

    def delete(self, item):
        self.__items.remove(item)

    def __iter__(self):
        return self.__items