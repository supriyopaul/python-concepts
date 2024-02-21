# Expert: Write a lambda function that takes a string as input and returns a new string with all consonants removed.
# Use this lambda function with the map() function to process a list of strings. The list of strings is ["apple", "banana", "cherry"]. What should the output be?

strings = ["apple", "banana", "cherry"]
remove_consonents = lambda s: "".join(l for l in s if l in "aeiou")

print(list(map(remove_consonents, strings)))
