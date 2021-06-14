from os import getcwd
from RedBlackTree import RedBlackTree


def print_size(tree):
    print(f"Size: {tree.get_size()}")


def print_height(tree):
    height = tree.get_height()
    print(f"Height: {height} ({height + 1} levels)")


try:
    print("Reading file data and inserting to tree...")
    tree = RedBlackTree()
    with open("EN-US-Dictionary.txt") as f:
        for word in f:
            tree.insert(word.rstrip('\n'))
except FileNotFoundError as e:
    print(e)
    print(f"Directory where the file is expected: '{getcwd()}'")
    exit()

while True:
    print('Press 1 to insert a word')
    print('Press 2 to print a size')
    print('Press 3 to print a height')
    print('Press 4 to search')
    print('Press 0 to exit')
    option = input('Your option: ')
    if option == '1':
        w = input('Enter the word: ')
        try:
            tree.insert(w)
        except Exception as e:
            print(e)
        print_size(tree)
        print_height(tree)
    elif option == '2':
        print_size(tree)
    elif option == '3':
        print_height(tree)
    elif option == '4':
        w = input('Enter the word to search: ')
        print('Found' if tree.search(w) else 'Not Found')
    elif option == '0':
        break
    else:
        print("Incorrect input.")
    print()
