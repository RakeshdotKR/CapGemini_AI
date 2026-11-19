# 2. Tuples: an ordered, immutable sequence — a fixed record whose shape you promise never to change.

# creation 
point = (3, 7)                          # 2-tuple
empty = ()                              # empty tuple
from_list = tuple([1, 2, 3])            # (1, 2, 3) — any iterable → tuple
from_string = tuple("hi")               # ('h', 'i')

#one-element tuple REQUIRES the trailing comma
a = (42,)                               # tuple
b = (42)                                # just the int 42 — parentheses are grouping!
c = 42,                                 # comma also creates a tuple (unparenthesised)
print(type(a), type(b), type(c))        # output: <class 'tuple'> <class 'int'> <class 'tuple'>

# immutability: no item assignment, no append 
# point[0] = 99                        # TypeError: 'tuple' object does not support item assignment (commented)

#immutability is SHALLOW 
row = (1, "gpt-4o", [100, 200])         # tuple containing a LIST
row[2].append(300)                      # legal — we mutated the LIST, not the tuple
print(row)                              # output: (1, 'gpt-4o', [100, 200, 300])
# RULE: a tuple locks its STRUCTURE (positions/length), not the objects it points at.

# hashability: what may live where 
# Tuples are hashable ONLY if every element is hashable:
ok_hash = (1, "two", (3, 4))            # fine — all immutable
# bad_hash = ([1, 2],)                  # TypeError: unhashable type: 'list' (commented)
print(hash(ok_hash) is not None)        # output: True

# That is exactly why tuples (not lists) can be dict keys or set members:
lookup = {(0, 0): "origin", (1, 2): "step"}
print(lookup[(1, 2)])                   # output: step