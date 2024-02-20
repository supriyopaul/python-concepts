'''
Write a dictionary comprehension that takes the list ages = [25, 30, 35, 40, 45] and maps each age to a boolean value indicating whether the age is even. What should the output be?
Input: ages = [25, 30, 35, 40, 45] Output: {25: False, 30: True, 35: False, 40: True, 45: False}
'''
ages = [25, 30, 35, 40, 45]
even_ages = {age:bool(age%2==0) for age in ages}

if __name__ == "__main__":
    print(even_ages)
