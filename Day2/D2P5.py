# Packing & unpacking

coords = (10,20,30) #packing
x,y,z = coords #unpacking
# print(x,y,z)

# star unpacking
first, *rest = (1,2,3,4)
# print(first, rest)

# unpacking on iterable
first_char, *tail_chars = "hello"
print(first_char,tail_chars)
