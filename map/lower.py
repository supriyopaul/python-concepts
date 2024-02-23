'''
For the list `sentences = ['The cat is black.', 'The dog is brown.']`, use `map` to create a new list where each sentence is converted to lowercase.
The expected output is `['the cat is black.', 'the dog is brown.']`
'''
sentences = ['The cat is black.', 'The dog is brown.']
print(list(map(lambda s: s.lower(), sentences)))
