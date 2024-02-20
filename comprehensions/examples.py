original_list = [1, 2, 3, 4, 5]

# Squaring each number in a list
lst = [x**2 for x in original_list]

# Creating a dictionary with number-square pairs
dct = {x: x**2 for x in original_list}

# Creating a set of even numbers
st = {x for x in original_list if x%2 ==0}

if __name__ == "__main__":
    print(lst)
    print(dct)
    print(st)