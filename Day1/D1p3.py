# Datatypes:
token_count = 1500
price_per_1k = 0.0025
total_cost = token_count /1000 * price_per_1k
batch_size = 37
# print(total_cost,type(total_cost))
context_window = 128_000 
# print(context_window)
# print(7/2)
# print(7//2) #floor division
# print(7%2)
# print(2**2)

# String: 
prompt = "Summarize the following in 3 bullet points:"
empty = ""
multiline = """Line 1
Line 2"""
# String access by index
# print(prompt[0])
# print(prompt[-1])
# print(prompt[0:5])
# print(len(prompt))
# print(multiline)

# Bool
# is_cached = True
# has_api_key = False

# if has_api_key: # int True == 1 | False == 0
#     print("Yes")
# else:
#     print("No")

# None
last_response = None
# print(last_response is None)

# Type conversion: Explicit conversion
age_str = "22"
age_int = int(age_str)
# print(type(age_int))
price_float = float("3.14")
# print(type(price_float))

tokens_str = str(1500)
cost_str = str(0.00375)

# print(int(3.99))
# print(round(3.99))
# print(int(-3.99))
# print(bool("false"),bool(""))
# print(bool(0),bool(42))

temperature = "0.7"
if not isinstance(temperature,(int,float)):
    temperature = float(temperature)
# print(f"temperature ok: {temperature}({type(temperature).__name__})")

# f strings
model,tokens,cost = "gpt-4o-mini",1500,0.00375
print(f"Model={model} | tokens={tokens} | cost=${cost:.6f}") #prints the values of model,tokens,cost
print(f"{'label':<12} | {'value':>10}")
print(f"Progress: {75:3d}%")
print(f"Heading:{'='*40}")