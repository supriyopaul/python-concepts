'''
For a list of tuples `coordinates = [(3,  2), (1,  1), (2,  3)]`, use `sorted` with a key argument and the `reverse` argument set to `True` to sort the list by the first element of each tuple in descending order.
The expected output is `[(3,  2), (2,  3), (1,  1)]`
'''

coordinates = [(3,  2), (1,  1), (2,  3)]
print(sorted(coordinates, reverse=True))