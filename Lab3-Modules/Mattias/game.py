from enum import Enum
import time
import colorama
from colorama import Back, Style
from functools import reduce

from ..bug import Bug, Rotation

WINDOW_SIZE = 30

colorama.init(autoreset=False)

class Color(Enum):
    WHITE = 0
    BLACK = 1

class Tile:
    def __init__(self) -> None:
        self.color = Color.WHITE

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class Ant(Bug):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def move(self, tile: Tile) -> None:
        if tile.color == Color.BLACK:
            self._turn(Rotation.COUNTER_CLOCKWISE)
        else:
            self._turn(Rotation.CLOCKWISE)

        tile.color = Color.BLACK if tile.color == Color.WHITE else Color.WHITE

        self._step()

    @property
    def symbol(self) -> str:
        return 'm '

class GameBoard:
    def __init__(self):
        self.tiles: dict[(int, int), Tile] = dict()
        self.bugs = [Ant(20, 20), Ant(5, 20)]

    def play(self, rounds = 20):
        print('\x1b[2J')
        for _ in range(0, rounds):
            self.print()
            for bug in self.bugs:
                bug.move(self.__get_tile(bug.y, bug.x))

            time.sleep(0.1)

            
    
    def print(self):
        print('\033[1;1H')
        for y in range(0, WINDOW_SIZE):
            colors = [self.__color(self.__get_tile(y,x)) for x in range(0,WINDOW_SIZE)]
            text = ['  ']*WINDOW_SIZE
            for bugs in [b for b in self.bugs if b.y == y and b.x >= 0 and b.x < WINDOW_SIZE]:
                text[bugs.x] = bugs.symbol

            print(reduce(lambda l,c: f'{l}{c[0]}{c[1]}', zip(colors, text), '') + Style.RESET_ALL, flush=True)
                            
    def __color(self, tile: Tile):
        return Back.CYAN if tile.color == Color.BLACK else Back.GREEN

    def __get_tile(self, y: int, x: int):
        return self.tiles.setdefault((y, x), Tile())

        
GameBoard().play(500)
