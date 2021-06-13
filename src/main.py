from RedBlackTree import RedBlackTree
# Read file Data
words = []
tree = RedBlackTree()
with open("EN-US-Dictionary.txt") as f:
    for word in f:
        tree.insert(word.rstrip('\n'))

while True:

    print('Press 1 to insert a word')
    print('Press 2 to print a size')
    print('Press 3 to print a height')
    print('Press 4 to search')
    print('Press 0 to save & exit')
    option = input('Your option : ')
    if option == '1':
        w = input('Enter the word : ')
        try:
            tree.insert(w)
        except Exception as e:
            print(e)
    elif option == '2':
        print(tree.get_size())
    elif option == '3':
        print(tree.get_height())
    elif option == '4':
        w = input('Enter the word to search : ')
        try:
            print(tree.search(w))
        except Exception as e:
            print(e)
    else:
        break
