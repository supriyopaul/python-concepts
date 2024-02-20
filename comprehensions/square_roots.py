'''
Given the list squares = [1, 4, 9, 16, 25], write a list comprehension to create a new list that contains the square root of each number in squares. What should the output be?
Input: squares = [1, 4, 9, 16, 25] Output: [1.0, 2.0, 3.0, 4.0, 5.0]
'''
from math import sqrt

squares = [1, 4, 9, 16, 25]
square_roots = [sqrt(number) for number in squares]

if __name__ == "__main__":
    print(square_roots)