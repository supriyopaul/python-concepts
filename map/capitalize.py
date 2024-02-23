'''
For the list `words = ['apple', 'banana', 'cherry']`, use `map` to create a new list where each word is capitalized.
The expected output is `['Apple', 'Banana', 'Cherry']`.
'''

words = ['apple', 'banana', 'cherry']
capitalize = lambda s: s[0].upper() + s[1:len(s)+1]
print(list(map(capitalize, words)))