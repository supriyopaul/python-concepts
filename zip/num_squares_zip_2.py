'''
Given two lists `numbers = [1, 2, 3, 4, 5]` and `squares = [1, 4, 9, 16, 25]`, use `zip` to create a new list where each element is a tuple of a number and its square.
The expected output is `[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]`.
'''

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

print(list(zip(numbers, squares)))