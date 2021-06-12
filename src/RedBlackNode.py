from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2


class RedBlackNode:
    def __init__(self, color, value, parent):
        self.color = color
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def change_color(self):
        self.color = Color.RED if self.color == Color.BLACK else Color.BLACK

    def search(self, value):
        if self.value == value:
            return True
        if self.value > value:
            return self.left is not None and self.left.search(value)
        return self.right is not None and self.right.search(value)
