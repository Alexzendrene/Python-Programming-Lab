a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def add_numbers(x, y):
    return x + y
  
result = add_numbers(a, b)
print('The addition of the two numbers is : ', result)

c = int(input("Enter the third number: "))

def multiply_numbers(x, y):
    return x * y

output = multiply_numbers(result, c)
print('The final output of the program is:', output)
