import pygame

import math

import random

from vertex import Vertex

from point import Point

class Figure:
    def __init__(self) -> None:
        self.vertices = []
        
        self.line_colors = [
            "#0079FF",
            "#00DFA2",
            "#F6FA70",
            "#FF0060",
        ]

    def draw(self, surface):
        for vertex in self.vertices:
            vertex.draw(surface)

    def add_vetex_by_mouse(self):
        (x, y) = pygame.mouse.get_pos()

        self.vertices.append(Vertex(x, y))

    def get_center(self):
        x_sum = sum([ vertex.center.x for vertex in self.vertices ])
        y_sum = sum([ vertex.center.y for vertex in self.vertices ])

        x_mean = x_sum / len(self.vertices)
        y_mean = y_sum / len(self.vertices)

        return Point(x_mean, y_mean)

    def stroke(self, surface):
        figure_center = self.get_center()

        def angle(point):
            return math.atan2(
                point.y - figure_center.y, 
                point.x - figure_center.x
            )

        vertices = [ vertex.center for vertex in self.vertices ]

        vertices.sort(key = angle)
        
        vertices_len = len(vertices)

        for i in range(vertices_len):
            start = vertices[i]
            end = vertices[(i + 1) % vertices_len]

            pygame.draw.aaline(
                surface,
                random.choice(self.line_colors),
                (int(start.x), int(start.y)),
                (int(end.x), int(end.y))
            )
