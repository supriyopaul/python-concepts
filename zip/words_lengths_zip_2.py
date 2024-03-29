'''
For the lists `words = ['hello', 'world']` and `lengths = [5, 5]`, use `zip` to create a new list where each element is a tuple of a word and its length.
The expected output is `[('hello', 5), ('world', 5)]`.
'''

words = ['hello', 'world']
print(list(zip(words, list(zip(words, list(map(lambda x: len(x), words)))))))