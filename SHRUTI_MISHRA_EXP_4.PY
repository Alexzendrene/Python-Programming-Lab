# Experiment - 4

def print_series(x, n):
    series_sum = sum(x ** i for i in range(n + 1))
    print(f"The series 1 + x + x^2 + ... + x^{n} = {series_sum}")

# declaring the variables and taking the input
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

# printing the serise 
print_series(x, n)
