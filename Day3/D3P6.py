from typing import Callable

def greet(name:str, times: int = 1)->str:
    return (name + " ") * times

def process(items: list[int],callback:Callable[[int],int]=None)->int:
    if callback is None:
        callback = lambda x: x * 2
    return sum(callback(i) for i in items) #expects another function as an argument

def pair(a:int,b:int)-> tuple[int,str]:
    return (a,b)

def maybe(x:int | None)-> int:
    return x if x is not None else 0

print(repr(greet("Hi",2))) #
print(process([1,2,3]))
# print(pair(1,"a"))
# print(maybe(None), type(maybe("5")))
