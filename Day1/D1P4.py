# Operators:
# Comparison operator
x = 10
# print(x == 10, x!=10, x>5,x>=10,x<3,x<=9)

# Chained comparison
age = 25
# print(18 <= age <=65)
score = 87
# print(80 < score <= 90)

# Logical operators
# print(True and False)  #Truth Table 
# print(True or False)
# print(not True)

name = None
display = name or "anonymous"
retries = 0
max_r = retries or 3
# print(display)
# print(max_r)

# Membership & identity operators : in / not in str, list, tuple, set, dict
models = {"gpt-4o-mini", "claude", "ollama"}
# print("gpt-4o-mini" in models)
# print("gpt-4o-mini" not in models)

# is / is not : compare OBJECT IDENTITY
response = None
# print(response is None)
# print(response == None)

a = [1,2]
b = [1,2]
c = a
# print(a == b) # comparing values
# print(a is b) # comparing objects
# print(a is c) # True: Same objects

# Walrus operator: assign AND use in one expression 
# data = "temperature=0.7"
# if (idx:= data.find("=")) !=-1: #assignment ins ide the condition
#     print(f"Value after '=': {data[idx+1:]}")

# Walrus operator: Assignment Expression operator | It allowing to assign to a variable 
# & use the value within the same expression
name = input("Enter your name")
if name:
    print(f"Hello {name}")

if name:= input("Enter your name"):
    print(f"Hello {name}")








