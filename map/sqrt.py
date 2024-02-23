'''
Given the list `squares = [1,  4,  9,  16,  25]`, use `map` to create a new list where each square is the square root of the number.
The expected output is `['1.0', '2.0', '3.0', '4.0', '5.0']`
'''
from math import sqrt

squares = [1,  4,  9,  16,  25]
print(list(map(sqrt, squares)))