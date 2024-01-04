def encrypt(e):
    a = 'abcdefghijklmnopqrstuvwxyz'
    l = ""
    for char in e:
        if char in a:
            x = a.index(char)
            l = l + a[(x + 2) % 26]  # Shift right by 2 positions in the alphabet
        else:
            l = l + char 
    return l

def decrypt(e):
    a = 'abcdefghijklmnopqrstuvwxyz'
    l = ""
    for char in e:
        if char in a:
            x = a.index(char)
            l = l + a[(x - 2) % 26]  # Shift left by 2 positions in the alphabet
        else:
            l = l + char  
    return l

input_str = input("Enter the string to be encrypted: ")
encrypted_str = encrypt(input_str)
print("Encrypted:", encrypted_str)

decrypted_str = decrypt(encrypted_str)
print("Decrypted:", decrypted_str)