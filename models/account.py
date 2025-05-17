from time import time

from containers.registry import AccountRegistry, CharacterRegistry
from character import Character, CharacterError

class Account:
    def __init__(self, email: str, timestamp: float = None):
        self.email = email
        self.__created_ts = timestamp if timestamp else time()
        self.__characters = CharacterRegistry()

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
        if self.__characters:
            self.__characters.add(char)

        return char

    def delete_character(self, char: Character) -> int:
        if char not in self.__characters:
            raise CharacterError("This character doesn't exist in this context.")

        self.__characters.delete(char)
        return 1

    @property
    def characters(self) -> CharacterRegistry:
        return self.__characters

    @property
    def created(self) -> float:
        return self.__created_ts

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