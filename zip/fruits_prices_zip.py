'''
For the lists `fruits = ['apple', 'banana', 'cherry']` and `prices = [1.0, 0.5, 2.0]`, use `zip` to create a new list where each element is a tuple of a fruit and its price.
The expected output is `[('apple', 1.0), ('banana', 0.5), ('cherry', 2.0)]`.
'''

fruits = ['apple', 'banana', 'cherry']
prices = [1.0, 0.5, 2.0]

print(list(zip(fruits, prices)))
