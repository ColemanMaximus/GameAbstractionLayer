from time import time
from inventory import PlayerInventory

class CharacterError(Exception):
    pass


class Character:
    max_name_length = 18

    def __init__(self, account, name: str, timestamp: float = None, inventory = None):
        self.account = account
        self.name = name
        self.__created_ts = timestamp if timestamp else time()
        self.__inventory = inventory if inventory else PlayerInventory(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if not _is_name_valid(name):
            raise ValueError(
                f"Provided name is invalid or exceeds the {self.max_name_length} character length."
            )

        self.__name = name

    @property
    def created(self) -> float:
        return self.__created_ts

    @property
    def inventory(self):
        return self.__inventory

    def __str__(self):
        return self.name


def _is_name_valid(name: str) -> bool:
    if not name.strip() or len(name) > Character.max_name_length:
        return False

    return True