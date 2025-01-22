'''6. bytearray([source[, encoding[, errors]]]): Returns a mutable sequence of 
bytes.It can be created from a string, a sequence of integers,
    or an object implementing the buffer interface.'''
# Creating a bytearray from a string
data = "Data"
byte_array = bytearray(data, 'utf-8')
print(byte_array)

# Modifying the bytearray
byte_array[0] = 68  # ASCII value of 'D'
print(byte_array)

# Appending a byte
byte_array.append(33)  # ASCII value of '!'
print(byte_array)

# Converting back to bytes
immutable_bytes = bytes(byte_array)
print(immutable_bytes)
