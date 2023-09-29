import pygame

from point import Point

class Vertex:
    def __init__(self, x, y) -> None:
        self.center = Point(x, y)
        self.r = 15
        self.color = (255, 255, 255)

    def __repr__(self):
        return str(self.center)

    def draw(self, surface):
        pygame.draw.circle(
            surface, 
            self.color, 
            self.center.to_tuple(),
            self.r, 
            1
        )

        pygame.draw.circle(
            surface, 
            self.color, 
            self.center.to_tuple(),
             1
        )
