'''
Given the list `numbers = [1,  2,  3,  4,  5]`, use `reduce` to find the difference between the maximum and minimum number.
The expected output is `4`
'''

from functools import reduce

numbers = [1,  2,  3,  4,  5]
print(reduce(max, numbers) - reduce(min, numbers))