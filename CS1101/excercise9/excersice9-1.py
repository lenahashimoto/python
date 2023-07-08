file = 'sample.txt'

with open(file, 'r') as fin:
    text = fin.read().split()


for word in text:
    if len(word) > 19:
        print(word)


def has_no_e(file):
    no_e = []
    for word in file:
        if 'e' not in word:
            no_e.append(word)
    percentage = round((len(no_e) / len(text)) * 100, 2)
    print(percentage, '%', 'of words has e.')

has_no_e(text)