'''
For the list `words = ['hello', 'world']`, use `map` to create a new list where each word is reversed. The expected output is `['olleh', 'dlrow']`.
'''

words = ['hello', 'world']
print(list(map(lambda s: s[::-1], words)))