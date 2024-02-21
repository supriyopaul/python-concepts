# Intermediate-Advanced: Write a lambda function that takes a list of numbers and returns a new list with each number squared. Use this lambda function in a list comprehension to process the list [1, 2, 3, 4, 5]. What should the output be?

original_list = [1, 2, 3, 4, 5]
squared = [(lambda x: x**2)(x) for x in original_list]
print(squared)
