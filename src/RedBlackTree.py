from RedBlackNode import RedBlackNode, Color


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.__checked_node = None
        self.size = 0

    def search(self, value):
        return self.root is not None and self.root.search(value)

    def get_size(self):
        return self.size

    def insert(self, value):
        self.size += 1
        if self.root is None:
            self.root = RedBlackNode(Color.BLACK, value, None)
            self.__checked_node = self.root
            return
        else:
            self.bst_insert(self.root, value, None)
            while self.__checked_node != self.root:
                if self.__checked_node.parent.color != Color.RED:
                    break
                p = self.__checked_node.parent
                g = self.__checked_node.parent.parent
                if p.right == self.__checked_node:
                    u = g.left
                    # case 3.a
                    if u is not None:
                        if u.color == Color.RED:
                            p.change_color()
                            u.change_color()
                            g.change_color()
                        self.__checked_node = g
                    # case 3.b
                    if u is None or u.color == Color.BLACK:
                        # case 3.b1
                        if g.right == p and p.right == self.__checked_node:
                            self.left_rotate(g)
                            p.change_color()
                            g.change_color()
                        # case 3.b2
                        if g.right == p and p.left == self.__checked_node:
                            self.right_rotate(p)
                else:
                    u = g.right
                    # case 3.a
                    if u is not None:
                        if u.color == Color.RED:
                            p.change_color()
                            u.change_color()
                            g.change_color()
                        self.__checked_node = g

                    # case 3.b
                    if u is None or u.color == Color.BLACK:
                        # case 3.b1
                        if g.left == p and p.left == self.__checked_node:
                            self.right_rotate(g)
                            p.change_color()
                            g.change_color()
                        # case 3.b2
                        if g.right == p and p.left == self.__checked_node:
                            self.left_rotate(p)
            self.root.color = Color.BLACK

    def bst_insert(self, node, value, parent):
        if node is None:
            new_node = RedBlackNode(Color.RED, value, parent)
            self.__checked_node = new_node
            return new_node
        if node.value < value:
            node.right = self.bst_insert(node.right, value, node)
        else:
            node.left = self.bst_insert(node.left, value, node)
        return node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.keft = y
        y.right = x
        x.parent = y


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.insert(6)
    tree.insert(7)
    print('Done...')
    