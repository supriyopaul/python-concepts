'''
Given the list `numbers = [1,  2,  3,  4,  5]`, use `reduce` to find the product of all numbers.
The expected output is `120`
'''

from functools import reduce

numbers = [1,  2,  3,  4,  5]

print(reduce(lambda a, b: a*b, numbers))
