from enum import Enum


class StatusRequirement(Enum):
    REQUESTED = 1
    IN_PROGRESS = 2
    WAITING_USER_RESPONSE = 3
    COMPLETED = 4
    ERROR = 5
