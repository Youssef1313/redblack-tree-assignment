from RedBlackNode import RedBlackNode, Color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def _search(self, node, value):
        if node.value == value:
            return True
        if node.value > value:
            return node.left is not None and self._search(node.left, value)
        return node.right is not None and self._search(node.right, value)

    def search(self, value):
        return self.root is not None and self._search(self.root, value)

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode(Color.BLACK, value, None)
            return
