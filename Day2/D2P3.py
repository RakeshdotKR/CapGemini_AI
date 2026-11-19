# Advanced list concepts

#  unpacking inside a for-loop header 
pairs = [("x", 10), ("y", 20), ("z", 30)]
for key, value in pairs:                 # each 2-tuple unpacked automatically
    print(f"{key}={value}", end=" ")     # output: x=10 y=20 z=30
print()

#  starred unpacking: "everything else" 
first, *rest = [10, 20, 30, 40]
print(first, rest)              # output: 10 [20, 30, 40]

head, *middle, tail = [1, 2, 3, 4, 5]
print(head, middle, tail)       # output: 1 [2, 3, 4] 5

# * in a function CALL spreads elements into arguments
def draw(x, y, color):
    return f"{color}@({x},{y})"
print(draw(*[10, 20, "red"]))   # output: red@(10,20)

# * in an assignment COLLECTS leftovers (complement of unpacking)
first, *others = range(5)
print(first, others)            # output: 0 [1, 2, 3, 4]

#  building lists efficiently 
# AVOID: repeated concatenation in a loop — O(n^2) because every += copies
big = []
for i in range(1000):
    big = big + [i]             # works, but quadratic — do not do this on large data

# PREFER: append in a loop (amortised O(1) each), or a comprehension
big = []
for i in range(1000):
    big.append(i)               # O(1) amortised per append
big = [i for i in range(1000)]  # comprehensions are faster still (Section 5)

#  membership on big lists: measure the difference 
import time

data = list(range(0, 1_000_000, 7))         # ~143k ints (multiples of 7)
probe = 999_999                             # 7 × 142857 → present at the very end

t0 = time.perf_counter()
found = probe in data                       # O(n) linear scan
t_list = time.perf_counter() - t0

fast = set(data)                            # O(n) ONCE
t0 = time.perf_counter()
found_fast = probe in fast                  # O(1) hash lookup
t_set = time.perf_counter() - t0

print(f"list: {found} in {t_list*1000:.2f} ms | set: {found_fast} in {t_set*1000:.2f} ms")