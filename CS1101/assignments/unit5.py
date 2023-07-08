def my_sqrt(a):
    x = a #initialize x with the value of a
    while True:
        y = (x + a/x) / 2 #calculate y using a and x values
        if y == x:  #cheke whether x and y are exactly equal
            return x #return the final value of x
            break
        x = y #update x with y


import math

def test_sqrt():
    a = 1 #initialize a
    while a <= 9:  #loop for a value from 1 to 9
        my_value = my_sqrt(a) 
        math_value = math.sqrt(a)
        abs_value = abs(my_value - math_value) #the absolute value of the diffrence between my_value and math_value
        print('a =', a, '|', 'my_sqrt(a) =', my_value,'|','math.sqrt(a) =', math_value,'diff =', abs_value)
        a = a + 1 #update a

def test_sqrt_modified():
    a = 1 #initialize a
    while a <= 25: #loop for a value from 1 to 25
        my_value = my_sqrt(a) 
        math_value = math.sqrt(a)
        abs_value = abs(my_value - math_value) #the absolute value of the diffrence between my_value and math_value
        print('a =', a, '|', 'my_sqrt(a) =', my_value,'|','math.sqrt(a) =', math_value,'diff =', abs_value)
        a = a + 1 #update a