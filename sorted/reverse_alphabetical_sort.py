'''
For a list of strings `strings = ['apple', 'Banana', 'Cherry']`, use `sorted` with the `reverse` argument set to `True` to sort the list in descending alphabetical order.
The expected output is `['Cherry', 'Banana', 'apple']`.
'''

strings = ['apple', 'Banana', 'Cherry']
print(sorted(strings, key=lambda s:s.upper(), reverse=True))
