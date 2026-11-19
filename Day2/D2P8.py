# Dictionary: an ordered mapping of hashable keys -> values.
# O(1) average lookup.

# Create
config = {"model":"gpt-4o-mini","temperature":0.2, "max_tokens":500}

empty = {}

from_pairs = dict([("a",1),("b",2),("c",3)])
# print(from_pairs)

# Zip
zipped = dict(zip(["k1","k2","k3"],[10,20,30]))
# print(zipped)

# print(dict(zip(["a","b","c"],[1])))

from_keys = dict.fromkeys(["read","write"],20)
# print(from_keys)

# Reading Values
config = {"model":"gpt-4o-mini","temperature":0.2, "max_tokens":0}
# print(config["model"])

# print(config.get("models","gemini-2.5-flash")) #safer approach
# print(config.get("max_tokens") or 500)  #unsafe approach

# updating, merging, removing
d = {"x":1,"y":2}
d.update({"y":99})
d.update(w=4)  #keyword form
# print(d)

left = {"a": 1,"b":2}
right = {"b": 10,"c":20}
# print(left|right)

# unpacking
print({**left, **right})                  # output: {'a': 1, 'b': 20, 'c': 3}

# chained merge 
defaults = {"model": "gpt-4o-mini", "temp": 0.2, "stream": True}
file_cfg = {"temp": 0.7}
cli_cfg  = {"model": "gpt-4o"}
effective = {**defaults, **file_cfg, **cli_cfg}
# print(effective)                          # output: {'model': 'gpt-4o', 'temp': 0.7, 'stream': True}
# print(defaults)

# removal 
d2 = {"a": 1, "b": 2, "c": 3}
# print(d2.pop("b"))                       
# print(d2.pop("zz", "fallback"))         
# d2.pop("zz")                         
del d2["a"]                              
# print(d2)                               

d3 = {"k": 1, "m": 2}
print(d3.popitem())                     

d = {"a": 1, "b": 2, "c": 3}

#  convert to lists when you need a snapshot / indexing 
print(list(d.keys()))                   
print(list(d.values()))                  
print(list(d.items()))                   

#  membership: `in d` tests KEYS  
print("a" in d)                          
print(1 in d)                           
print(1 in d.values())                  
print("zz" not in d)                    
