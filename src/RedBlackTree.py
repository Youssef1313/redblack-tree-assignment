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

    def insert(self, value):
        if self.root is None:
            # Tree is empty. Insert a black root.
            self.root = RedBlackNode(Color.BLACK, value, None)
            return

        leaf = self._search(self.root, value)
        if leaf.value == value:
            raise ValueError(f"The value '{value}' already exists.")

        new_node = RedBlackNode(Color.RED, value, leaf)
        if value > leaf.value:
            leaf.right = new_node
        else:
            leaf.left = new_node
        if leaf.color == Color.RED:
            self._fixup(new_node)

    def _get_uncle(self, node):
        grandparent = node.parent.parent
        if grandparent is None:
            raise ValueError("This is unexpected!")
        if node.parent is grandparent.left:
            return grandparent.right
        return grandparent.left

    def _fixup(self, node):
        if node.color != Color.RED or node.parent.color != Color.RED:
            raise ValueError("Expected a red node with a red parent to fix.")
        uncle = self._get_uncle(node)
        # Case 1:
        if uncle is not None and uncle.color == Color.RED:
            # If uncle is red, we recolor parent, uncle.
            # Also recolor grantparent, but only if it's not the root.
            uncle.change_color()
            node.parent.change_color()
            if node.parent.parent is not self.root:
                node.parent.parent.change_color()

            if node.parent.parent.color == Color.RED and\
               node.parent.parent.parent.color == Color.RED:
                self._fixup(node.parent.parent)
            return

        # Case 2.1 followed by case 3
        #    5(B)              5(B)
        #   /   \             /   \
        # NIL  7(R)  ====>  NIL  6(R)
        #      /                   \
        #    6(R)                  7(R)
        if node is node.parent.left and\
           node.parent is node.parent.parent.right:
            # Recolor the nodes 6 and 5 in the example.
            node.change_color()
            node.parent.parent.change_color()

            # rotate 7(R) node in the example above.
            self.right_rotate(node.parent)

            # rotate 5(B) node in the example above.
            self.left_rotate(node.parent)
            return

        # Case 2.2
        #    5(B)              5(B)
        #   /   \             /   \
        #  3(R)  NIL  ====>  4(R)  NIL
        #   \                /
        #   4(R)            3(R)
        if node is node.parent.right and\
           node.parent is node.parent.parent.left:
            node.change_color()
            node.parent.parent.change_color()

            # rotate 3(R) node in the example above.
            self.left_rotate(node.parent)

            # rotate 5(B) node in the example above.
            self.right_rotate(node.parent)
            return

        # Case 3.1
        #    5(B)              3(B)
        #   /   \             /   \
        #  3(R)  NIL  ====>  2(R)  5(R)
        #  /
        # 2(R)
        if node is node.parent.left and\
           node.parent is node.parent.parent.left:
            node.parent.change_color()
            node.parent.parent.change_color()
            self.right_rotate(node.parent.parent)
            return

        # Case 3.2
        #   5(B)                6(B)
        #  /   \               /   \
        # NIL   6(R)   ====>  5(R)   7(R)
        #        \
        #        7(R)
        if node is node.parent.right and\
           node.parent is node.parent.parent.right:
            node.parent.change_color()
            node.parent.parent.change_color()
            self.left_rotate(node.parent.parent)
            return

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
            x.parent.left = y
        y.right = x
        x.parent = y

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
