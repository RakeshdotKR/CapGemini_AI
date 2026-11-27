def countdown(n):
    while n>0:
        yield n
        n-=1

gen = countdown(3)
print(list(gen))
print(list(gen))

def evens(stop):
    for i in range(stop):
        if i % 2 == 0:
            yield i

print(list(evens(7)))