from RedBlackTree import RedBlackTree
# Read file Data
tree = RedBlackTree()
with open("EN-US-Dictionary.txt") as f:
    for word in f:
        tree.insert(word.rstrip('\n'))

while True:

    print('Press 1 to insert a word')
    print('Press 2 to print a size')
    print('Press 3 to print a height')
    print('Press 4 to search')
    print('Press 0 to exit')
    option = input('Your option : ')
    if option == '1':
        w = input('Enter the word : ')
        try:
            tree.insert(w)
        except Exception as e:
            print(e)
        print(f"Size: {tree.get_size()}")
        print(f"Height: {tree.get_height()}")
    elif option == '2':
        print(f"Size: {tree.get_size()}")
    elif option == '3':
        print(f"Height: {tree.get_height()}")
    elif option == '4':
        w = input('Enter the word to search : ')
        print(tree.search(w))
    else:
        break
