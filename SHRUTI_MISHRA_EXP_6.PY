# Q --> count the letters of the string and store them in a dictionary

str= input("Enter the string:")
f={}

for i in str:
    if i in f:
        f[i] += 1
    else:
        f[i]= 1

print(f)
