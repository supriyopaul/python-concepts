'''
Given two lists `fruits = ['apple', 'banana', 'cherry']` and `colors = ['red', 'yellow', 'red']`, use `zip` to create a new list where each element is a tuple of a fruit and its color.
The expected output is `[('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')]`
'''

fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'red']

print(list(zip(fruits, colors)))
