'''
For the list `ages = [25,  30,  35,  40]`, use `reduce` to find the least common multiple (LCM) of all numbers.
The expected output is `60`
'''


from functools import reduce
from math import lcm

ages = [25,  30,  35,  40]
print(reduce(lcm, ages))
