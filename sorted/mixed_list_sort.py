'''
For a list of mixed data types `mixed_list = [5, 'apple',  3.14, 'banana']`, use `sorted` to sort the list.
The expected output is `[3.14,  5, 'apple', 'banana']`
'''

mixed_list = [5, 'apple',  3.14, 'banana']
print(sorted(mixed_list, key=lambda x: str(x)))