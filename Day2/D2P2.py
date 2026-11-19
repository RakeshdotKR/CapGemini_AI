# Aliasing vs copying
import copy
original = [[1,2],[3,4]]

alias = original # Two names, ONE object

sliced = original[:]     #SHALLOW copy: NEW outer list, SAME inner objects
copied = original.copy()

deep = copy.deepcopy(original) # DEEP COPY: new inner objects

alias.append([99])
print(original)

sliced[0].append(77)
print(original)

print(deep)

