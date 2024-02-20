'''
Given the list prices = [1.99, 4.50, 3.49, 2.75, 5.25], write a set comprehension to create a set of prices that are greater than 3. What should the output be?
Input: prices = [1.99, 4.50, 3.49, 2.75, 5.25] Output: {4.5, 5.25}
'''

prices = [1.99, 4.50, 3.49, 2.75, 5.25]
greater_than_3 = {p for p in prices if p > 3.0}

if __name__ == "__main__":
    print(greater_than_3)