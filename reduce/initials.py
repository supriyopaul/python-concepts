'''
For the list `words = ['hello', 'world']`, use `reduce` to create a single string that contains the first letter of each word.
The expected output is `'hwo'`
'''

from functools import reduce

words = ['hello', 'world']
print(reduce(lambda x, y: x[0]+y[0], words))