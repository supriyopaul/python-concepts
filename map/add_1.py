'''
For the list `numbers = [1,  2,  3,  4,  5]`, use `map` to create a new list where each number is incremented by  1. The expected output is `[2,  3,  4,  5,  6]`
'''

numbers = [1,  2,  3,  4,  5]
print(list(map(lambda n: n+1, numbers)))