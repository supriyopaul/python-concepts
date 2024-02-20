'''
Given the list numbers = [5, 10, 15, 20, 25], write a list comprehension to create a new list that contains the negative of each number in numbers. What should the output be?
Input: numbers = [5, 10, 15, 20, 25] Output: [-5, -10, -15, -20, -25]
'''
numbers = [5, 10, 15, 20, 25]
negative_numbers = [0-num for num in numbers]

if __name__ == "__main__":
    print(negative_numbers)