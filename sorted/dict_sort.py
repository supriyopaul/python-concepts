'''
Given a list of dictionaries `students = [{'name': 'Alice', 'age':  20}, {'name': 'Bob', 'age':  22}, {'name': 'Charlie', 'age':  18}]`, use `sorted` with a key argument to sort the list by the 'age' key.
The expected output is `[{'name': 'Charlie', 'age':  18}, {'name': 'Alice', 'age':  20}, {'name': 'Bob', 'age':  22}]`
'''
students = [{'name': 'Alice', 'age':  20}, {'name': 'Bob', 'age':  22}, {'name': 'Charlie', 'age':  18}]
print(sorted(students, key=lambda x: x['age']))
