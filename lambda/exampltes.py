# A basic lambda function that adds two numbers.
add = lambda x, y: x+y
print(add(1, 2))


# Intermediate: Lambda with Conditional Logic
# A lambda function that returns True if a number is even, False otherwise.
is_even = lambda x: bool(x%2==0)
print(is_even(101))


# Intermediate-Advanced: Lambda in List Comprehension
# Using a lambda function inside a list comprehension to square numbers in a list.
numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x**2)(x) for x in numbers]
print(squared)


# Advanced: Lambda with map()
# Using a lambda function with map() to convert temperatures from Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40]
celsius_to_fahrenhiet = lambda c: (9/5)*c+32
fahrenheit = map(celsius_to_fahrenhiet, celsius)
print(list(fahrenheit))

# Expert: Lambda with filter() and map()
# Using a lambda function with filter() and map() to find squares of even numbers in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = lambda x: x**2
is_even = filter(lambda x: bool(x%2==0))
even_squares = map(square, is_even, numbers)
print(list(even_squares))