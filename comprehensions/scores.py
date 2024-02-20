'''
Write a dictionary comprehension that takes the list students = ['Alice', 'Bob', 'Charlie'] and maps each student's name to a score of 0. What should the output be?
Input: students = ['Alice', 'Bob', 'Charlie'] Output: {'Alice': 0, 'Bob': 0, 'Charlie': 0}
'''
students = ['Alice', 'Bob', 'Charlie']
scores = {s:0 for s in students}

if __name__ == "__main__":
    print(scores)
