'''
For the lists `words = ['apple', 'banana', 'cherry']` and `lengths = [5, 6, 6]`, use `zip` to create a new list where each element is a tuple of a word and its length.
The expected output is `[('apple', 5), ('banana', 6), ('cherry', 6)]
'''

words = ['apple', 'banana', 'cherry']
print(list(zip(words, list(map(lambda word: len(word), words)))))