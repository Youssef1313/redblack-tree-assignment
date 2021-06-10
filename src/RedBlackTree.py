from RedBlackNode import RedBlackNode


class RedBlackTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self.root is not None and self.root.search(value)

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode('b', value, None)
