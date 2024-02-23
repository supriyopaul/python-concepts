'''
Given the list `ages = [25,  30,  35,  40]`, use `map` to create a new list where each age is multiplied by  1.5.
The expected output is `[37.5,  45.0,  52.5,  60.0]`
'''
ages = [25,  30,  35,  40]
print(list(map(lambda num: 1.5*num, ages)))