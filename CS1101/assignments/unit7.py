alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d


#Part 1

def has_duplicates(s):
     #loop over the values in histogram
     for value in histogram(s).values():
        #return True if there is a value more than 2
        if value >= 2:
            return True
     return False

#A function that loops over the strings in the provided list
def check_duplicates(t):
     for item in t:
          #One of the condition runs based on a result of has_duplicates
          if has_duplicates(item) == True:
               print(item, 'has duplicates')
          else:
               print(item, 'has no duplicates')


#Part 2

def missing_letters(s):
    #initialize a variable missing for missing letters
    missing = []
    #loop over each letter in alphabet
    for letter in alphabet:
        #if a letter is in the given string skip the letter
        if letter in histogram(s).keys():
            pass
        #add the letter to a list of missing
        else:
            missing.append(letter)
        #return concatenated strings
    return ''.join(missing)

#A function that loops over the strings in the provided list
def check_missing_letters(t):
    #loop over each string in the provided list t
    for item in t:
        #One of the condition runs based on a result of missing_letters
        if missing_letters(item) == '':
            print(item, 'uses all the letters')
        else:
            print(item, 'is missing letters', missing_letters(item))