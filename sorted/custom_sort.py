'''
Given a list of strings containing both numbers and non-numeric characters `mixed_strings = ['apple', '42', 'banana', '17', 'cherry']`, use sorted with a custom sorting function to sort the list in a way that numeric elements are treated as integers and sorted numerically, while non-numeric elements are sorted alphabetically.
The expected output is `['apple', 'banana', 'cherry', '17', '42']`
'''

mixed_strings = ['apple', '42', 'banana', '17', 'cherry']
print(sorted(mixed_strings, key=lambda x: (float("inf"), x) if x.isnumeric() else (float("-inf"), x)) )