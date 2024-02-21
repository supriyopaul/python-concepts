# Advanced: Write a lambda function that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit. Use this lambda function with the map() function to convert a list of temperatures from Celsius to Fahrenheit. The list of temperatures is [0, 10, 20, 30, 40]. What should the output be?

temperatures = [0, 10, 20, 30, 40]
c2f = lambda c: (9/5)*c + 32
print(list(map(c2f, temperatures)))