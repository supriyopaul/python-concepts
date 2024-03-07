'''
Given a list of tuples `grades = [('Alice',  85), ('Bob',  90), ('Charlie',  80)]`, use `sorted` with a key argument to sort by the second element of each tuple.
The expected output is `[('Charlie',  80), ('Alice',  85), ('Bob',  90)]`.
'''

grades = [('Alice',  85), ('Bob',  90), ('Charlie',  80)]
print(sorted(grades, key=lambda x: x[1]))