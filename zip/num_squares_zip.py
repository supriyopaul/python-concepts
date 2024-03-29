'''
For the lists `numbers = [1, 2, 3]` and `squares = [1, 4, 9]`, use `zip` to create a new list where each element is a tuple of a number and its square.
The expected output is `[(1, 1), (2, 4), (3, 9)]`.
'''

numbers = [1, 2, 3]
squares = [1, 4, 9]

print(list(zip(numbers, squares)))