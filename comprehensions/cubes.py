'''
Given the list numbers = [10, 15, 20, 25, 30], write a list comprehension to create a new list that contains the cube of each number in numbers. What should the output be?
Input: numbers = [10, 15, 20, 25, 30] Output: [1000, 3375, 8000, 15625, 27000]
'''

numbers = [10, 15, 20, 25, 30]
cubes = [x**3 for x in numbers]

if __name__ == "__main__":
    print(cubes)