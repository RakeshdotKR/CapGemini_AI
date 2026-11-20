# unpacking when calling functions
def power(base, exponent):
    return base ** exponent

positional = (2,10)
keywords = {"base":2, "exponent":5}

print(power(*positional))
print(power(**keywords))
print(power(*[5],**{"exponent":5}))