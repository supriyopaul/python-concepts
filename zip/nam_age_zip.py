'''
Given two lists `names = ['Alice', 'Bob', 'Charlie']` and `ages = [25, 30, 35]`, use `zip` to create a new list where each element is a tuple of a name and an age.
The expected output is `[('Alice', 25), ('Bob', 30), ('Charlie', 35)]`
'''
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print(list(zip(names, ages)))