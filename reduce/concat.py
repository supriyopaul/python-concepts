'''
Given the list `words = ['apple', 'banana', 'cherry']`, use `reduce` to concatenate all words into a single string.
The expected output is `'applebananacherry'`
'''

from functools import reduce

words = ['apple', 'banana', 'cherry']
print(reduce(lambda x, y: x+y, words))