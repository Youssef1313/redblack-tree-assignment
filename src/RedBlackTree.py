import sys
from RedBlackNode import RedBlackNode, Color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def _search(self, node, value):
        if node.value == value:
            return node
        if node.value > value:
            if node.left is None:
                return node
            return self._search(node.left, value)

        if node.right is None:
            return node
        return self._search(node.right, value)

    def search(self, value):
        return self.root is not None and\
               self._search(self.root, value).value == value

    def fixup(self, node):
        if self.root is node:
            return self.root.change_color()\
                if self.root.color == Color.RED else None

        # case 0: parent is black no problem
        if not isinstance(node, RedBlackNode) or\
           node.parent.color == Color.BLACK:
            return
        '''
        no need to check that the grand parent is not None since
        if it is not exist then the parent will be the root and must be black
        so we won't reach this line.
        '''
        # case 1: uncle y is red
        grand_parent = node.parent.parent
        if grand_parent.left is not None and\
           grand_parent.right is not None and\
           grand_parent.right.color == grand_parent.left.color == Color.RED:

            grand_parent.change_color()
            grand_parent.right.change_color()
            grand_parent.left.change_color()
            return self.fixup(grand_parent)

        # case 2: uncle y is black, node is a right child
        # case 3: uncle y is black, node is a left child
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

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode(value, Color.BLACK, None)
            return

        node = self._search(self.root, value)
        if node.value == value:
            return

        new_node = RedBlackNode(value, parent=node)
        if node.value > value:
            node.left = new_node
        else:
            node.right = new_node
        self.fixup(new_node)

    def rotate_left(self, x):
        if not isinstance(x, RedBlackNode):
            return

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
        self.root = y if self.root is x else self.root

    def rotate_right(self, y):
        if not isinstance(y, RedBlackNode):
            return

        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent
        if y is not self.root:
            if y.parent.right is y:
                y.parent.right = x
            else:
                x.parent.left = x

        y.parent = x
        x.left = y
        self.root = x if self.root is y else self.root

    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == Color.RED else "BLACK"
            print(str(node.value) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)


# tree = RedBlackTree()
# tree.insert(11)
# tree.insert(3)
# tree.insert(13)
# tree.insert(1)
# tree.insert(7)
# tree.insert(15)
# tree.insert(5)
# tree.insert(8)
# tree.pretty_print()

tree = RedBlackTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.insert(7)
