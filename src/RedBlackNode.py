from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2


class RedBlackNode:
    def __init__(self, value, color=Color.RED,
                 parent=None, left=None, right=None):

        self.color = color
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def change_color(self):
        self.color = Color.RED if self.color == Color.BLACK else Color.BLACK
