from abc import ABC, abstractmethod
from enum import IntEnum

class Direction(IntEnum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3

class Rotation(IntEnum):
    CLOCKWISE = 1,
    COUNTER_CLOCKWISE = -1

class Bug(ABC):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.__direction = Direction.NORTH
        self.__x = x
        self.__y = y

    @abstractmethod
    def move(self) -> None:
        pass

    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def _turn(self, direction: Rotation):
        self.__direction = Direction((self.__direction - direction) % len(Direction))

    def _step(self):
        self.__x = self.__x + {
            Direction.NORTH: 0,
            Direction.EAST: 1,
            Direction.SOUTH: 0,
            Direction.WEST: -1
        }[self.__direction]

        self.__y = self.__y + {
            Direction.NORTH: -1,
            Direction.EAST: 0,
            Direction.SOUTH: 1,
            Direction.WEST: 0
        }[self.__direction] 




