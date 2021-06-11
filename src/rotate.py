from RedBlackNode import RedBlackNode
from RedBlackTree import RedBlackTree


def left_rotate(tree, x):
    if not (isinstance(tree, RedBlackTree) and isinstance(x, RedBlackNode)):
        return None

    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x

    y.parent = x.parent
    if x is not tree.root:
        if x.parent.right is x:
            x.parent.right = y
        else:
            x.parent.left = y

    x.parent = y
    y.left = x
