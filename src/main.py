# Read file Data
words = []
with open("EN-US-Dictionary.txt") as f:
    for word in f:
        words.append(word.rstrip('\n'))
