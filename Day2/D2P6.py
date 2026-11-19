# Sets: unordered collection of unique, hashable elements

# Creation
tags = {"billing", "urgent", "bug"}
dups = {1,2,2,3,3,3}
from_list = set([1,2,2,3])
letters = set("capgemini")

# print(tags)
# print(dups)
# print(from_list)
# print(letters)

# print(sorted(letters))

# adding
tags.add("features")
# print(tags)
tags.update(["ui","api","features"])
# print(tags)


frontend = {"css","html","js","ReactJS","Python"}
backend = {"FastAPI","SpringBoot","js","Python"}

# print(sorted(frontend | backend)) #union
print(sorted(frontend & backend)) #Intersection
# print(sorted(backend - frontend)) #difference

# print({"js"}<=frontend) #subset
# print(frontend>={"js","html"})# superset
# print(frontend.isdisjoint({"GenAi"}))