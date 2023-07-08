def expectedValue(x, px):
    r = len(x)
    total = 0
    for i in range(x):
        singleValue = x[i]*px[i]
        total = total + singleValue
    return total

import math

def stdDiv(x, px):
    mu = expectedValue(x, px)
    r = len(x)
    total = 0
    for i in range(r):
        squared = (x[i] - mu)**2*px[i]
        total = total + squared
        result = math.sqrt(total)
    return result