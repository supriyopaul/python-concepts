'''
Given a list of dictionaries `students = [{'name': 'Alice', 'age':  20}, {'name': 'Bob', 'age':  22}, {'name': 'Charlie', 'age':  18}]`, use `sorted` with a key argument and the `reverse` argument set to `True` to sort the list by the 'age' key in descending order.
The expected output is `[{'name': 'Bob', 'age':  22}, {'name': 'Alice', 'age':  20}, {'name': 'Charlie', 'age':  18}]`
'''

students = [{'name': 'Alice', 'age':  20}, {'name': 'Bob', 'age':  22}, {'name': 'Charlie', 'age':  18}]
print(sorted(students, key=lambda x:x["age"], reverse=True))