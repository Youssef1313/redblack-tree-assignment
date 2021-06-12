from RedBlackNode import RedBlackNode, Color


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _search(self, node, value):
        if node.value == value:
            return True
        if node.value > value:
            return node.left is not None and self._search(node.left, value)
        return node.right is not None and self._search(node.right, value)

    def search(self, value):
        return self.root is not None and self._search(self.root, value)

    def get_size(self):
        return self.size

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode(Color.BLACK, value, None)
            node = self.root
            self.size += 1
            return
        else:
            node = self.bst_insert(self.root, value)
            while node != self.root:
                if node.parent.color != Color.RED:
                    break
                p = node.parent
                g = node.parent.parent
                if p.right == node:
                    u = g.left
                    # case 3.a
                    if u is not None:
                        if u.color == Color.RED:
                            p.change_color()
                            u.change_color()
                            g.change_color()
                        node = g
                    # case 3.b
                    if u is None or u.color == Color.BLACK:
                        # case 3.b1
                        if g.right == p and p.right == node:
                            self.left_rotate(g)
                            p.change_color()
                            g.change_color()
                        # case 3.b2
                        if g.right == p and p.left == node:
                            self.right_rotate(p)
                else:
                    u = g.right
                    # case 3.a
                    if u is not None:
                        if u.color == Color.RED:
                            p.change_color()
                            u.change_color()
                            g.change_color()
                        node = g

                    # case 3.b
                    if u is None or u.color == Color.BLACK:
                        # case 3.b1
                        if g.left == p and p.left == node:
                            self.right_rotate(g)
                            p.change_color()
                            g.change_color()
                        # case 3.b2
                        if g.right == p and p.left == node:
                            self.left_rotate(p)
            self.root.color = Color.BLACK
        self.size += 1


    def bst_insert(self, node, value):
        if node.value == value:
            raise ValueError("The value is already in the tree.")
        if node.value < value:
            if node.right is None:
                new_node = RedBlackNode(Color.RED, value, node)
                node.right = new_node
                return new_node
            return self.bst_insert(node.right, value)
        # Here we know that node.value > value
        if node.left is None:
            new_node = RedBlackNode(Color.RED, value, node)
            node.left = new_node
            return new_node
        return self.bst_insert(node.left, value)

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
