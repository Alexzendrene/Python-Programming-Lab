'''file = open("EXP_15.txt", "r")
# Read the first 7 characters of the FIRST line and print them
data = file.readline(7)
print(data, end="")

file.close()'''



file = open("EXP_15.txt", "r")
while True:
    data = file.readline()
    if not data:
        break
    print(data, end="")

file.close()