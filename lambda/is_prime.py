# Expert: Write a lambda function that takes a number as input and returns True if the number is prime, False otherwise.
# Use this lambda function with the filter() function to find all prime numbers in the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. What should the output be?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_prime = lambda num: all(num%n!=0 for n in range(2, num))
print(list(filter(is_prime, numbers)))