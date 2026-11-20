def greet(name, greeting = "Hello"):
    """Return a greeting string for the given name"""
    return f"{greeting},{name}"

# print(greet("Rakesh"))
# print(greet("Rakesh",greeting="Hi"))
print(greet.__name__,"|",greet.__doc__)