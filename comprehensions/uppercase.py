'''
Create a set comprehension that takes the list letters = ['a', 'b', 'c', 'A', 'B', 'C'] and includes only the uppercase letters. What should the output be?
Input: letters = ['a', 'b', 'c', 'A', 'B', 'C'] Output: {'A', 'B', 'C'}
'''
letters = ['a', 'b', 'c', 'A', 'B', 'C']
uppercase_letters = {letter.upper() for letter in letters}

if __name__ == "__main__":
    print(uppercase_letters)