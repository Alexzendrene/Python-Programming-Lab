# Q1 --> use of return keyword if the print function does the same work.

# the function declaring and calling
'''
def sum():
    #print(a+b)
    return(a+b)
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
x=sum()
print(x)
'''

# function declaring and passing variable.
'''
def greet(name):
    print("Good Morning", name)
greet("Rohan")
'''

# function declaring and passing 2 parameters.
# positional argument
# you can not change the position of argument.
#Number of parameters = number of arguments
'''
def greet(fname, lname):
    print("Good Morning", fname, lname)
greet("Shruti","Mishra")
'''

# keyword argunment
# order is not important
#Number of parameters = number of arguments
# it should follow positional argument
'''
def greet(fname,lname):
    print("Good Morning", fname, lname)
greet("Mishra", lname="Shruti")
'''

# DEFAULT ARGUMENT
'''
def greet(fname="Guest"):
    print("Good Morning", fname)
# if you pass [greet("Rohan")] output is Rohan 
# if passing [greet()] output is guest
greet("Rohan")
'''

# VARIABLE LENGTH ARGUMENT
# we use it when we dont kmow the number of argument
# if we use * its the tuple
'''
def greet(*args):
    print(args)
    print(len(args))
    print(type(args))
greet("India","USA","Russia","Saudi Arabia")
'''
# if we use ** its the dictionary
'''
def greet(**args):
    print(args)
    print(len(args))
    print(type(args))
greet(fname='Shruti', lname='Mishra')
'''
#greet('Shruti', 'Mishra')  it give error

# Q2 --> to print the factorial number with and without using factorial
# create factorial function 

# Q3 --> write a program for calculator (/,*,-,+) do not simply call enter the first number and also enter the symbol like he opt 3 then + the 5
# create a calculator which takes the operational symbols of (/,*,-,+) and  take input from the user.
# for signs create dictionary , then enter 2 nos, then use for loop, pick an operation from operations then other input number.
# like 1+2 = 3 then we want to 3 * 2 = 6 (operation can be any)



num = int(input("Enter the Number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)