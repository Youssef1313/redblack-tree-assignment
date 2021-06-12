from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2


class RedBlackNode:
    def __init__(self, color, value, parent):
        self._color = color
        self._value = value
        self._parent = parent
        self._left = None
        self._right = None

    def change_color(self):
        self._color = Color.RED if self._color == Color.BLACK else Color.RED

    # Only getters for now. Add setters ONLY when needed.

    @property
    def color(self):
        return self._color

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right
