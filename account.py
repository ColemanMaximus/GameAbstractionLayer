from time import time
from typing import List

from registry import Registry
from character import Character, CharacterError

class AccountRegistry(Registry):
    def __init__(self):
       super().__init__()

    @property
    def accounts(self):
        return self._items

    def __iter__(self):
        return self._items

class Account:
    def __init__(self, email: str):
        self.email = email
        self.__created_timestamp = time()
        self.__characters = []

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        if not _is_email_valid(email):
            raise ValueError("Provided email is invalid.")

        self.__email = email

    def create_character(self, name: str):
        char = Character(self, name)
        self.__characters.append(char)

        return char

    def delete_character(self, char: Character) -> int:
        if char not in self.__characters:
            raise CharacterError("This character doesn't exist in this context.")

        self.__characters.remove(char)
        return 1

    @property
    def characters(self) -> List[Character]:
        return self.__characters

    @property
    def created_timestamp(self) -> float:
        return self.__created_timestamp

    @classmethod
    def create(cls, email: str, registry: AccountRegistry = None):
        account = cls(email)
        if registry:
            registry.add(account)

        return account

    @classmethod
    def delete(cls, account, registry: AccountRegistry) -> int:
        registry.delete(account)
        return 1

def _is_email_valid(email: str) -> bool:
    if not email.strip() or "@" not in email:
        return False

    return True