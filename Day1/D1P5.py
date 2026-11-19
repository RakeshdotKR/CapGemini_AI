# Control Statements
temperature = 0.7 # 0-1

if temperature < 0.3:
    mode = "deterministic"

elif temperature < 0.8:
    mode = "balanced"

else:
    mode = "creative"

# print(f"Temperature= {temperature} -> {mode}")

# Nested if
access = False
is_admin = True
if is_admin:
    if True:
        access = True

# Ternary operator
status = "allowed" if is_admin else "denied"
# print(status)

# Loops:
for i in range(5):
    print(i,end= " ")
print()

for i in range(2, 11, 2):
    print(i,end= " ")
print()

for ch in "LLM":
    print(ch,end="-")
print()

total, count = 0,0
for n in [10,20,30,40]:
    total += n
    count += 1
print(f"sum={total},count={count},")

# While loops:
attempts, max_attempts = 0, 5
while attempts < max_attempts:
    attempts += 1
    print(f"attempt {attempts} of {max_attempts}")

#    