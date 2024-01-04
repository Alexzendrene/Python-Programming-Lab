import random

# Example 1: Generating a random integer between a range
random_integer = random.randint(1, 10)  
print("Random Integer:", random_integer)

# Example 2: Generating a random floating-point number between 0 and 1
random_float = random.random()  
print("Random Float:", random_float)

# Example 3: Generating a random choice from a list
my_list = ["apple", "banana", "cherry", "date", "fig"]
random_choice = random.choice(my_list)  
print("Random Choice:", random_choice)

# Example 4: Shuffling a list randomly
random.shuffle(my_list)  
print("Shuffled List:", my_list)

# using the seed() 
random.seed(10)
print(random.random())

# getstate() and setstate()
list1 = [1, 2, 3, 4, 5]  
  
# capture the current state
# using the getstate() method
state = random.getstate()
  
# Prints list of random items of given length 
print(random.sample(list1, 3)) 
  
# restore the captured state
# using the setstate() method
# pass the captured state as the parameter
random.setstate(state)
  
# now printing the same list of random
# items
print(random.sample(list1, 3)) 

# Generate and print a random 4-bit number using getrandbits()
random_bits = random.getrandbits(4)
print("Random 4-Bit Number:", bin(random_bits)[2:].zfill(4))
