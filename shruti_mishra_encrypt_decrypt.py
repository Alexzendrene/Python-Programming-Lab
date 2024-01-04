def encrypt(e, b):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = ""
    for i in range(b):
        x = e[i]
        if x in a:
            y = a.index(x)
            l = l + a[(y + 2) % 26]  # Shift right by 2 positions in the alphabet
        else:
            l = l + x  
    return l

def decrypt(e, b):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = ""
    for i in range(b):
        x = e[i]
        if x in a:
            y = a.index(x)
            l = l + a[(y - 2) % 26]  # Shift left by 2 positions in the alphabet
        else:
            l = l + x  
    return l

b = input("Enter the string to be encrypted: ")
d = len(b)
encrypted_str = encrypt(b, d)
decrypted_str = decrypt(encrypted_str, d)
print("Original:", b)
print("Encrypted:", encrypted_str)
print("Decrypted:", decrypted_str)
