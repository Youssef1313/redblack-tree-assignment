from RedBlackNode import RedBlackNode, Color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self.root is not None and self.root.search(value)

    def fixup(self, node):
        # case 0: parent is black no problem
        if node.parent.color == Color.BLACK or\
             not isinstance(node, RedBlackNode):
            return None

        # case 1: uncle y is red
        grand_parent = node.parent.parent
        if grand_parent.right.color == grand_parent.left.color == Color.RED:
            grand_parent.change_color()
            grand_parent.right.change_color()
            grand_parent.left.change_color()
            return self.fixup(grand_parent)

        # case 2: uncle y is black, node is a right child
        # case 3: uncle y is black, node is a left child
        if grand_parent.right.color != grand_parent.left.color:
            if grand_parent.left is node.parent:
                if node.parent.right is node:
                    self.rotate_left(node.parent)
                self.rotate_right(grand_parent)

            else:
                if node.parent.left is node:
                    self.rotate_right(node.parent)
                self.rotate_left(grand_parent)

            node.parent.change_color()
            grand_parent.change_color()

        return self.root.change_color()\
            if self.root.color == Color.RED else None

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode(Color.BLACK, value, None)
            return None

        node = self.search(value)
        if node.value == value:
            return None

        new_node = RedBlackNode(value, parent=node)
        if node.value > value:
            node.left = new_node
        else:
            node.right = new_node
        self.fixup(new_node)

    def rotate_left(self, x):
        if not isinstance(x, RedBlackNode):
            return None

        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x is not self.root:
            if x.parent.right is x:
                x.parent.right = y
            else:
                x.parent.left = y

        x.parent = y
        y.left = x

    def rotate_right(self, x):
        # TODO: write it.
        pass
