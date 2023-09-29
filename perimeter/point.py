import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"P({ self.x }, { self.y })"

    def to_tuple(self):
        return (self.x, self.y)
