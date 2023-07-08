import math

def print_volume(r):
    volume = 4/3 * math.pi * r**3
    print(volume)

#import a random module
import random

def diagnosis(p1, p2):
    #return a random number between the range of 0 and 100
    num = random.randint(0, 100)
    #change the number of random_number to a string
    compatibility = str(num)
    #assign values of p1, p2, compatibility and put into a sentence
    message = "Compatibility of " + p1 + " and " + p2 + " is " + compatibility + "%"
    print(message)

diagnosis("Kate", "Bob")

diagnosis("Chocolate", "Banana")
