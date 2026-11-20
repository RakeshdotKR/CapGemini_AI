# lambda function
# square = lambda x,y=19: x * y
# print(square(6), square(9,2))

numbers = [5, 2, 9, 1, 7]
# print(list(map(lambda n: n * 2, numbers)))     # apply to every element
# print(list(filter(lambda n: n % 2 == 0, numbers))) # keep matching elements
# print(sorted(numbers))                                 # ascending
# print(sorted(numbers, reverse=True))                   # descending


#reduce (from `functools`) folds a sequence into a single accumulated value:

from functools import reduce

print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))       # (((1+2)+3)+4)
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))       # 24
print(reduce(lambda a, b: a if a > b else b, [3, 9, 2, 7]))  # maximum