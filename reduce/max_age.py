'''
For the list `ages = [25,  30,  35,  40]`, use `reduce` to find the maximum age. The expected output is `40`.
'''
from functools import reduce

ages = [25,  30,  35,  40]
print(reduce(lambda x, y: max(x, y), ages))