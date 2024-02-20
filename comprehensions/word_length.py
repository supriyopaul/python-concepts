'''
Create a dictionary comprehension that takes the list words = ['apple', 'banana', 'cherry'] and maps each word to its length. What should the output be?
Input: words = ['apple', 'banana', 'cherry'] Output: {'apple': 5, 'banana': 6, 'cherry': 6}
'''

words = ['apple', 'banana', 'cherry']
word_lengths = {word:len(word) for word in words}

if __name__ == "__main__":
    print(word_lengths)
