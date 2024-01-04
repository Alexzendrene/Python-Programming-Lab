# Function to perform Caesar encryption
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Function to perform Caesar decryption
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
while True:
    input_string = input("Enter a string: ")
    choice = input("Encrypt (e) or Decrypt (d)? Enter 'e' or 'd': ")

    if choice == 'e':
        shift = int(input("Enter the shift value for encryption: "))
        encrypted_text = encrypt(input_string, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        shift = int(input("Enter the shift value for decryption: "))
        decrypted_text = decrypt(input_string, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

    exit_choice = input("Do you want to exit (yes/no)? ").lower()
    if exit_choice == "yes":
        break