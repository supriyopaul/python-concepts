# Expert: Write a lambda function that takes a list of strings as input and returns a new list with all strings sorted in alphabetical order.
# Use this lambda function with the map() function to process a list of strings. The list of strings is ["orange", "apple", "banana", "cherry"]. What should the output be?

strings = ["orange", "apple", "banana", "cherry"]
sort_strings = lambda strings: sorted(strings)
print(sort_strings(strings))
