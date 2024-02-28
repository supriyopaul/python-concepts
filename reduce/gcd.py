'''
Given the list `squares = [1,  4,  9,  16,  25]`, use `reduce` to find the greatest common divisor (GCD) of all numbers.
The expected output is `1`.
'''

from functools import reduce
from math import gcd

squares = [1,  4,  9,  16,  25]
print(reduce(gcd, squares))

