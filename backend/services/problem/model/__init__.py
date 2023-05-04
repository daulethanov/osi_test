from enum import Enum


class ActJob(Enum):
    pending = 'В ожидании'
    start = 'В работе'
    finish = 'Выполнено'
