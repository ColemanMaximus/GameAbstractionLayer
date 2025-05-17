class CharacterError(Exception):
    pass

class Character:
    max_name_length = 18

    def __init__(self, account, name: str):
        self.account = account
        self.name = name

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

    def __str__(self):
        return self.name

def _is_name_valid(name: str) -> bool:
    if not name.strip() or len(name) > Character.max_name_length:
        return False

    return True