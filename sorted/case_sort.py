'''
For a list of strings `strings = ['apple', 'Banana', 'Cherry']`, use `sorted` with a key argument to sort the list in case-insensitive alphabetical order.
The expected output is `['apple', 'Banana', 'Cherry']`
'''

strings = ['apple', 'Banana', 'Cherry']
print(sorted(strings, key=lambda x: x.lower()))