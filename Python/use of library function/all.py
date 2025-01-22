'''2. all(iterable): Returns True if all elements of the iterable are true 
    (or if the iterable is empty). Equivalent to:


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
    I DO NOT UNDERSTAND THIS FUNCTION

# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

# result = all(a)  # Pass the list 'a' as the argument
# print(result)  # This will print True
    '''
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

c = [x == y for x, y in zip(a, b)]  # Compare each element in a and b
print(all(c))  # This will print True
print(any(c))