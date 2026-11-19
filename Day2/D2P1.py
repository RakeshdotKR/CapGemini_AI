# Create list
empty = []
models = ["gpt-4o","claude-3","ollama"]
mixed = [1,"two",3.0,True,None]
nested = [[1,2],[3,4]]

from_range = list(range(1,6))
unpacked = list((8,9,10))

# Repetition
row = [0] * 5

# Repeating a LIST copies the REFERENCE, not the content
grid = [row] * 3
grid[0][0] = 99
# print(grid)

#build the rows with a comprehension so each row is a NEW list
grid_ok = [[0]*3 for _ in range(3)]
grid_ok[0][1] = 99
# print(grid_ok)

# list() on any iterable
# print(list("xyz"))
# print(list({"x":1,"y":2}))
# print(list(iter([1, 2, 3])))

# Indexing, Slicing & stride
#index  0   1   2   3   4   5
nums = [10, 20, 30, 40, 50, 60]
#index -6   -5  -4  -3  -2  -1

# basic indexing
# print(nums[0]) #first element
# print(nums[-1]) #last element
# print(nums[101]) #IndexError

# Slicing [start:stop:step]
# print(nums[1:4])
# print(nums[:2])
# print(nums[3:])
# print(nums[::2])
# print(nums[::-1])
# print(nums[100::]) #not to be used this way
# print(nums[-100:100]) #not to be used this way

# slice objects: 
s = slice(1,5,2) #slice object
# print(nums[s])
# print(s.indices(len(nums)))
# print(list(s.indices(3)))
# print(nums)

# slice assignment: replace, insert, delete
letters = ["a","b","c","d"]
letters[1:3] = ["x","y","z"] #mutable
# print(letters)

letters2 = ["a","b","c","d"]
letters2[1:3] = []
# print(letters2)

letters3 = ["a","b","c","d"]
letters3[1:1] = ["NEW"]
# print(letters3)

letters4 = ["a","b","c","d"]
letters4[::2] = ["1","2"]
# print(letters4)
letters4[::2] = ["CapGemini","CG"]
# print(letters4)

# List methods
tokens = [50,100,150]
# Adding
tokens.append(200) #O(1)
# print(tokens)

tokens.insert(0,400) #O(n)
# print(tokens)

tokens.extend([250,300]) #O(k) | append EACH element of any iterable
# print(tokens)

# append(list)
nested_demo = [1,2]
nested_demo.append([3,4])
# print(nested_demo)

flat_demo = [1,2]
flat_demo.extend([3,4])
# print(flat_demo)

# REMOVING 
stack = [1, 2, 3, 4]
# last = stack.pop()              # O(1) 
# print(last, stack)             

# front = stack.pop(1)            # O(n)
# print(front, stack)           

# stack.remove(3)                 # O(n) 
# print(stack)                   
# stack.remove(99)             # ValueError: list.remove(x): x not in list (commented)

# del stack[0]                    # O(n) 
# print(stack)                   

# stack.append(7); stack.append(7)
# stack.clear()                   # O(n) 
# print(stack)   

# Searching
nums = [3,1,4,4,1,5,9,2,6,4]
# print(nums.count(1)) 
# print(nums.index(4))
# nums(99) #ValueError
# print(4 in nums)

# Aggeragates
# print(len(nums), sum(nums), min(nums), max(nums))

# ordering
# print(nums.sort())  #O(n log n)
# print(nums.sort(reverse=True))

words = ["xyz","a","ccc","ggg","dd"]
# words.sort()
# print(words)
# words.sort(key=len)
# print(words)















