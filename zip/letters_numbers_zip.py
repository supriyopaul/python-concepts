'''
Given two lists `letters = ['a', 'b', 'c']` and `numbers = [1, 2, 3]`, use `zip` to create a new list where each element is a tuple of a letter and a number.
The expected output is `[('a', 1), ('b', 2), ('c', 3)]`.
'''

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

print(list(zip(letters, numbers)))
