n = 4  # Number of rows

for i in range(n, 0, -1):  # Iterate from n to 1 in reverse order
    for j in range(1, i + 1):  # Iterate from 1 to i
        # Print the numbers with a space, end="" to avoid newline
        print(j, end=" ")  
    print()  # Move to the next line after each row
