# EXPERIMENT 1
# AIM - To print the largest and the smallest number of two numbers.

# Take the numbers as the input
# float for decimal values 
# int for integer values
# if not specified by default string

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# using python function max() for finding the max of two nos.
largest = max(num1, num2)
# using python function min() for finding the min of two nos.
smallest = min(num1, num2)

# Printing the variable which stores the largest value.
print("Largest number:", largest)
# Printing the variable which stores the smallest value.
print("Smallest number:", smallest)
