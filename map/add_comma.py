'''
Given the list `names = ['Alice', 'Bob', 'Charlie']`, use `map` to create a new list where each name is followed by a comma and space.
The expected output is `['Alice, ', 'Bob, ', 'Charlie, ']`.
'''

names = ['Alice', 'Bob', 'Charlie']
print(list(map(lambda s: s+", ", names)))
