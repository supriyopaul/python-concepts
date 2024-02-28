'''
Given the list `temperatures = [0,  10,  20,  30]`, use `reduce` to find the minimum temperature. The expected output is `0`
'''

from functools import reduce

temperatures = [0,  10,  20,  30]
print(reduce(lambda x,y: x if x<y else y, temperatures))