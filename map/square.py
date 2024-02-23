'''
Given the list `numbers = [1,  2,  3,  4,  5]`, use `map` to create a new list where each number is squared.
The expected output is `[1,  4,  9,  16,  25]`.
'''

numbers = [1,  2,  3,  4,  5]
print(list(map(lambda x: x**2, numbers)))