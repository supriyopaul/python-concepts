'''
Create a set comprehension that takes the list words = ['apple', 'banana', 'cherry'] and includes only the words that start with 'b'. What should the output be?
Input: words = ['apple', 'banana', 'cherry'] Output: {'banana'}
'''
words = ['apple', 'banana', 'cherry']
starts_with_b = {word for word in words if word.startswith('b')}

if __name__ == "__main__":
    print(starts_with_b)