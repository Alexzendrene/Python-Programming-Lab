with open('filename.txt', 'r') as file:
    content = file.read()

with open('filename.txt', 'w') as file:
    file.write('Hello, World!')


with open('filename.txt', 'a') as file:
    file.write('Appending some text.')


with open('filename.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')


with open('filename.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()


with open('filename.txt', 'r+') as file:
    content = file.read()
    file.write('Appending some text.')


with open('binary_file.bin', 'rb') as binary_file:
    binary_data = binary_file.read()

with open('binary_file.bin', 'wb') as binary_file:
    binary_file.write(b'\x01\x02\x03')


with open('binary_file.bin', 'rb+') as binary_file:
    binary_data = binary_file.read()
    binary_file.write(b'\x04\x05\x06')

with open('binary_file.bin', 'wb+') as binary_file:
    binary_data = binary_file.read()
    binary_file.write(b'\x07\x08\x09')


with open('filename.txt', 'a+') as file:
    file.write('Appending some text.')
    file.seek(0)
    content = file.read()


with open('binary_file.bin', 'ab+') as binary_file:
    binary_file.write(b'\x04\x05\x06')
    binary_file.seek(0)
    binary_data = binary_file.read()


with open('filename.txt', 'r') as file:
    content = file.read()
    position = file.tell()
