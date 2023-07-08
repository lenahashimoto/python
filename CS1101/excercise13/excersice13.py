book = 'sample.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

print(words)

from string import punctuation, whitespace

print(punctuation)

def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    print(cleansed)
    return cleansed

print("{} has {} 'words'".format(book, len([clean(word) for word in words])))
