# Experinment - 3
# Input the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the sum to 0
total_sum = 0

# Use a loop to add the numbers from 1 to n terms
for i in range(1, n + 1):
    total_sum += i

# Print the sum from variable total_sum.
print("The sum of the series 1 + 2 + 3 + ... + ",n, "is:", total_sum )
