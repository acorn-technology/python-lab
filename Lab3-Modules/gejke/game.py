import pygame
from pygame.locals import *
from typing import Tuple

from ..bug import Bug, Rotation

class Ant(Bug):

    def __init__(self, x: int, y: int, color: Tuple[int, int, int]) -> None:
        super().__init__(x, y)
        self._color = color

    @property
    def pos(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @property
    def color(self) -> Tuple[int, int, int]:
        return self._color

    def move(self) -> None:
        self._step()

    def symbol(self) -> str:
        return super().symbol

    def __repr__(self):
        return "<Ant: x: {} - y: {}".format(self.x, self.y)

def step_ant(ant: Ant, screen):
    
    color = screen.get_at(ant.pos)
    if sum(color) == 255*4:
        ant._turn(Rotation.CLOCKWISE)
        screen.set_at(ant.pos, ant.color)
    else:
        ant._turn(Rotation.COUNTER_CLOCKWISE)
        screen.set_at(ant.pos, (255, 255, 255))
    ant.move()


WIDTH = 100
HEIGHT = 100


def main():
    ant = Ant(WIDTH//2, HEIGHT//2, (255, 0, 0))

    (width, height) = (800, 800)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('AntMan')

    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill((255,255,255))
    
    for _ in range(20000):
        step_ant(ant, surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(pygame.transform.scale(surface, screen.get_rect().size), (0, 0))
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    pygame.init()
    main()