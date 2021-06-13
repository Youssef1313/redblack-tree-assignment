from RedBlackNode import Color
import RedBlackTree


def empty_tree():
    tree = RedBlackTree.RedBlackTree()
    assert tree.root is None
    return tree


def test_empty_tree():
    tree = empty_tree()
    assert not tree.search(0)
    # assert tree.size == 0
    # TODO: assert height


def test_left_left():
    tree = empty_tree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    assert tree.search(1)
    assert tree.search(2)
    assert tree.search(3)
    assert not tree.search(4)
    # assert tree.size == 3
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 2
    assert root.parent is None
    left = root.left
    assert left.color == Color.RED
    assert left.value == 1
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.RED
    assert right.value == 3
    assert right.parent is root
    assert right.left is None
    assert right.right is None


def test_left_right():
    tree = empty_tree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    assert tree.search(1)
    assert tree.search(2)
    assert tree.search(3)
    assert not tree.search(4)
    # assert tree.size == 3
    root = tree.root
    assert root.parent is None
    assert root.color == Color.BLACK
    assert root.value == 2
    left = root.left
    assert left.color == Color.RED
    assert left.value == 1
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.RED
    assert right.value == 3
    assert right.parent is root
    assert right.left is None
    assert right.right is None


def test_right_left():
    tree = empty_tree()
    tree.insert(1)
    tree.insert(3)
    tree.insert(2)
    assert tree.search(1)
    assert tree.search(2)
    assert tree.search(3)
    assert not tree.search(4)
    # assert tree.size == 3
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 2
    assert root.parent is None
    left = root.left
    assert left.color == Color.RED
    assert left.value == 1
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.RED
    assert right.value == 3
    assert right.parent is None
    assert right.left is None
    assert right.right is None


def test_right_right():
    tree = empty_tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    assert tree.search(1)
    assert tree.search(2)
    assert tree.search(3)
    assert not tree.search(4)
    # assert tree.size == 3
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 2
    assert root.parent is None
    left = root.left
    assert left.color == Color.RED
    assert left.value == 1
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.RED
    assert right.value == 3
    assert right.parent is root
    assert right.left is None
    assert right.right is None


def test_left_uncle():
    tree = empty_tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    assert tree.search(1)
    assert tree.search(2)
    assert tree.search(3)
    assert tree.search(4)
    assert not tree.search(5)
    # assert tree.size == 4
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 2
    assert root.parent is None
    left = root.left
    assert left.color == Color.BLACK
    assert left.value == 1
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.BLACK
    assert right.value == 3
    assert right.parent is None
    assert right.left is None
    right_right = right.right
    assert right_right.color == Color.RED
    assert right_right.value == 4
    assert right_right.parent is right
    assert right_right.left is None
    assert right_right.right is None

    tree.insert(5)
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 2
    assert root.parent is None
    left = root.left
    assert left.color == Color.BLACK
    assert left.value == 1
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.BLACK
    assert right.value == 4
    assert right.parent is root
    right_left = right.left
    assert right_left.color == Color.RED
    assert right_left.value == 3
    assert right_left.parent is right
    assert right_left.left is None
    assert right_left.right is None
    right_right = right.right
    assert right_right.color == Color.RED
    assert right_right.value == 5
    assert right_right.parent is right
    assert right_right.left is None
    assert right_right.right is None


def test_right_uncle():
    tree = empty_tree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    assert tree.search(1)
    assert tree.search(2)
    assert tree.search(3)
    assert tree.search(4)
    assert not tree.search(5)
    # assert tree.size == 4
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 3
    assert root.parent is None
    left = root.left
    assert left.color == Color.BLACK
    assert left.value == 2
    assert left.parent is root
    left_left = left.left
    assert left_left.color == Color.RED
    assert left_left.value == 1
    assert left_left.parent is left
    assert left_left.left is None
    assert left_left.right is None
    assert left.right is None
    right = root.right
    assert right.color == Color.BLACK
    assert right.value == 4
    assert right.parent is root
    assert right.left is None
    assert right.right is None

    tree.insert(0)
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 3
    assert root.parent is None
    left = root.left
    assert left.color == Color.BLACK
    assert left.value == 1
    assert left.parent is root
    left_left = left.left
    assert left_left.color == Color.RED
    assert left_left.value == 0
    assert left_left.parent is left
    assert left_left.left is None
    assert left_left.right is None
    left_right = left.right
    assert left_right.color == Color.RED
    assert left_right.value == 2
    assert left_right.parent is left
    assert left_right.left is None
    assert left_right.right is None
    right = root.right
    assert right.color == Color.BLACK
    assert right.value == 4
    assert right.parent is root
    assert right.right is None
    assert right.left is None


def test_larger_case():
    tree = empty_tree()
    tree.insert(41)
    tree.insert(44)
    tree.insert(95)
    tree.insert(83)
    tree.insert(72)
    tree.insert(66)
    tree.insert(94)
    tree.insert(90)
    tree.insert(59)
    assert tree.search(41)
    assert tree.search(44)
    assert tree.search(95)
    assert tree.search(83)
    assert tree.search(72)
    assert tree.search(66)
    assert tree.search(94)
    assert tree.search(90)
    assert tree.search(59)
    assert not tree.search(5)
    # assert tree.size == 9
    root = tree.root
    assert root.color == Color.BLACK
    assert root.value == 44
    assert root.parent is None
    left = root.left
    assert left.color == Color.BLACK
    assert left.value == 41
    assert left.parent is root
    assert left.left is None
    assert left.right is None
    right = root.right
    assert right.color == Color.RED
    assert right.value == 83
    assert right.parent is root
    right_left = right.left
    assert right_left.color == Color.BLACK
    assert right_left.value == 66
    assert right_left.parent is right
    right_left_left = right_left.left
    assert right_left_left.color == Color.RED
    assert right_left_left.value == 59
    assert right_left_left.parent is right_left
    assert right_left_left.left is None
    assert right_left_left.right is None
    right_left_right = right_left.right
    assert right_left_right.color == Color.RED
    assert right_left_right.value == 72
    assert right_left_right.parent is right_left
    assert right_left_right.left is None
    assert right_left_right.right is None
    right_right = right.right
    assert right_right.color == Color.BLACK
    assert right_right.value == 94
    assert right_right.parent is right
    right_right_left = right_right.left
    assert right_right_left.color == Color.RED
    assert right_right_left.value == 90
    assert right_right_left.parent is right_right
    assert right_right_left.left is None
    assert right_right_left.right is None
    right_right_right = right_right.right
    assert right_right_right.color == Color.RED
    assert right_right_right.value == 95
    assert right_right_right.parent is right_right
    assert right_right_right.left is None
    assert right_right_right.right is None
