'''
For the list `temperatures = [0,  10,  20,  30]`, use `map` to create a new list where each temperature is converted to Fahrenheit.
The expected output is `[32,  50,  68,  86]`
'''
temperatures = [0,  10,  20,  30]
print(list(map(lambda t: (t * 9/5) + 32, temperatures))) 