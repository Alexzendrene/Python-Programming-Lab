# Strings to be used for different functions
string1 = "_Hello, World!_"
# Function to demonstrate various string functions

def string_functions(input_string):
    
    # Upper case
    upper_case = input_string.upper()
    print("Upper Case: ", upper_case)

    is_upper_case = upper_case.isupper()
    print("Is Upper Case: ", is_upper_case)

    is_lower_case = upper_case.islower()
    print("Is Lower Case: ", is_lower_case)

    # Lower case
    lower_case = input_string.lower()
    print("Lower Case: ", lower_case)

    is_upper_case = lower_case.isupper()
    print("Is Upper Case: ", is_upper_case)

    is_lower_case = lower_case.islower()
    print("Is Lower Case: ", is_lower_case)

    # Count characters 'a' in the string
    count_a = input_string.count('o')
    print("Count of 'o': ", count_a)

    # Title case (capitalize each word)
    title_case = input_string.title()
    print("Title Case: ", title_case)

    # Split the string into a list of words
    split_words = input_string.split()
    print("Split Words: ", split_words)

    # Strip leading and trailing whitespace
    stripped_string = input_string.strip('_')
    print("Stripped String: ", stripped_string)

    lstripped_string = input_string.lstrip('_')
    print("Left Stripped String: ", lstripped_string)

    rstripped_string = input_string.rstrip('_')
    print("Right Stripped String: ", rstripped_string)

    # Replace 'old' with 'new'
    replaced_string = input_string.replace('World', 'Python')
    print("Replaced String: ", replaced_string)
    
    join_string = ", ".join(input_string)
    print("Join String: ", join_string)

    starts_with = input_string.startswith("_Hello,")
    print("Start With: ", starts_with)
    
    ends_with = input_string.endswith("World!_")
    print("Ends With: ", ends_with)

# Demonstrate functions on different strings
string_functions(string1)
