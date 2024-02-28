'''
For the list `names = ['Alice', 'Bob', 'Charlie']`, use `reduce` to create a single string that contains all names separated by commas.
The expected output is `'Alice, Bob, Charlie'`
'''

from functools import reduce

names = ['Alice', 'Bob', 'Charlie']
print(reduce(lambda x, y: x+", "+y, names))