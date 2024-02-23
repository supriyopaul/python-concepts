'''
Given the list `numbers = [1,  2,  3,  4,  5]`, use `map` to create a new list where each number is converted to a string.
The expected output is `['1', '2', '3', '4', '5']`
'''
numbers = [1,  2,  3,  4,  5]
print(list(map(lambda num: str(num), numbers)))

