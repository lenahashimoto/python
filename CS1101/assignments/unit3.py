def health_indication():
    #a prompt asks the user to type the answer
    text = input('Which is your blood type; A, B, AB, or O?\n')

    #chained conditional.  The user can input either a capital or lowercase letter.
    if text == "A" or text == "a":
        print('Mosquitos are less attracted to you than to other blood types.')
    elif text == "B" or text == "b":
        print('Type B has 50,000 times the number of strains of friendly bacteria than A or O types')
    elif text == "AB" or text == "ab":
        print('Type AB+ is the universal plasma donor')
    elif text == "O" or text == "o":
        print('Type O can donate red blood cells to anyone and has Lower risk for pancreatic cancer')
    #in case of the user inputs an unexpected value.
    else:
        print("I don't know the blood type you input.")


def health_indication2():
    #a prompt asks the user to type the answer
    text = input('Which is your blood type; A, B, AB, or O?\n')

    #chained conditional.  The user can input either a capital or lowercase letter.
    if text == "A" or text == "a":
        print('Mosquitos are less attracted to you than to other blood types.')
    else:
        if text == "B" or text == "b":
            print('Type B has 50,000 times the number of strains of friendly bacteria than A or O types')
        else:
            if text == "AB" or text == "ab":
                print('Type AB+ is the universal plasma donor')
            else:
                if text == "O" or text == "o":
                    print('Type O can donate red blood cells to anyone and has Lower risk for pancreatic cancer')
                else:
                    print("I don't know the blood type you input.")

import datetime

today = datetime.date.today()
year = today.year
month = today.month
day = today.day
adult = "You are old enough to drink alchohol."
child = "You are too young to drink."

def check_age(yy, mm, dd):
    y = year - yy
    m = month - mm
    d = day - dd

    if (y >= 20 and m > 0) or (y == 20 and m == 0 and d < 0):
        print(adult)

    else:
        print(child)


def check_age(yy, mm, dd):
    y = year - yy
    m = month - mm
    d = day - dd

    if y > 20:
        print(adult)

    elif y < 20:
        print(child)

    else:
        if y == 20:
            if m > 0:
                print(adult)
            
            elif m < 0:
                print(child) 

            else:
                if d == 0:
                    print(adult)
                elif d < 0:
                    print(adult)
                else:
                    print(child)
