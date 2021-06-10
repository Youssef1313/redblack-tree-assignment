class RedBlackNode:
    def __init__(self, color, value, parent):
        if color != 'r' and color != 'b':
            raise ValueError("Node color must be either 'r' or 'b'.")
        self.color = color
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def change_color(self):
        self.color = 'r' if self.color == 'b' else 'r'

    def search(self, value):
        if self.value == value:
            return True
        if self.value > value:
            return self.left != None and self.left.search(value)
        return self.right != None and self.right.search(value)
