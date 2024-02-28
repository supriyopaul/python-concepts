'''
For the list `squares = [1,  4,  9,  16,  25]`, use `reduce` to find the sum of all squares. The expected output is `70`
'''
from functools import reduce
from math import sqrt

squares = [1,  4,  9,  16,  25]
print(reduce(lambda x, y: sqrt(x)+sqrt(y), squares))