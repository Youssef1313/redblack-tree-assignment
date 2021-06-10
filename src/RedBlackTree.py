from RedBlackNode import RedBlackNode, Color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self.root is not None and self.root.search(value)

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode(Color.BLACK, value, None)
            return
