from time import time
from enum import Enum


class ActionType(Enum):
    ACCOUNT_CREATE = "ACCOUNT_CREATE"
    CHARACTER_CREATE = "CHARACTER_CREATE"
    CHARACTER_DELETE = "CHARACTER_DELETE"
    CURRENCY_ADDED = "CURRENCY_ADDED"
    CURRENCY_REMOVED = "CURRENCY_REMOVED"
    SHOP_ITEM_BUY = "SHOP_ITEM_BUY"
    MAP_CELL_LOAD = "MAP_CELL_LOAD"
    MAP_ENTITIES_LOAD = "MAP_ENTITIES_LOAD"


class ActionStatusType(Enum):
    SUCCESS = "SUCCESS"
    PENDING = "PENDING"
    FAILED = "FAILED"
    ERROR = "ERROR"


class ActionStatus:
    def __init__(self, action_type: ActionStatusType):
        self.__type =  action_type

    @property
    def type(self) -> ActionStatusType:
        return self.__type

    @type.setter
    def type(self, status_type: ActionStatusType):
        self.__type = status_type


class Action:
    def __init__(self, action_type: ActionType):
        self.__type = action_type
        self.__timestamp = time()
        self.__status = ActionStatus(ActionStatusType.PENDING)

    @property
    def type(self) -> ActionType:
        return self.__type

    @property
    def status(self) -> ActionStatus:
        return self.__status

    @status.setter
    def status(self, status_type: ActionStatusType):
        self.__status.type = status_type

    @property
    def timestamp(self) -> float:
        return self.__timestamp

    def response(self, content = None):
        return ActionResponse(self, self.status, content)


class ActionResponse:
    def __init__(self, action: Action, status: ActionStatus, content = None):
        self.__action = action
        self.__status = status
        self.__timestamp = time()
        self.__content = content

    @property
    def action(self) -> Action:
        return self.__action

    @property
    def status(self) -> ActionStatus:
        return self.__status

    @property
    def timestamp(self) -> float:
        return self.__timestamp

    @property
    def content(self):
        return self.__content
