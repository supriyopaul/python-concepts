# Expert: Write a lambda function that takes a list of numbers as input and returns the sum of all numbers in the list.
# Use this lambda function with the reduce() function from the functools module to find the sum of the list [1, 2, 3, 4, 5]. What should the output be?

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_ = lambda x,y: x+y
print(reduce(sum_, numbers)) 