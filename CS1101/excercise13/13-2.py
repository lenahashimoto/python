from string import punctuation, whitespace

origin = 'book.txt'
# huck = 'huck.txt'
# frank = 'frank.txt'
# great = 'great.txt'
# meta = 'meta.txt'
sherlock = 'sherlock.txt'
# tale = 'tale.txt'

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def clean(word):
    result = ''
    for letter in word:
        if (letter in whitespace) or (letter in punctuation):
            pass
        else:
            result += letter.lower()
    return result

def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def frequent_word(d):
    countdonw = sorted(d)[::-1]
    top10 = countdonw[:10]
    top10List = []
    for k in top10:
        top10List.append([d[k], k])
    return top10List


def print_frq(d):
    for item in d:
        print("%s: %s times used" % (item[0], item[1]))


books = [origin, sherlock]

def stats():
    for book in books:
        book = open(book, 'r')
        print("Stats for %s:" % book.name)
        data = [clean(word) for word in words(book)]
        book.close()
        print("  Total: %s" % len(data))
        print("  Unique: %s" % len(histogram(data)))
        hist = invert_dict(histogram(data))
        frq_word = frequent_word(hist)
        print_frq(frq_word)
stats()
