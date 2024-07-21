# Day 14: 30 Days of python programming

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map applies a function to each element within a list
# filter returns elements within a list that result in true within a given function
# reduce returns a single value that is the result of repeatedly applying elements of a list

# higher order functions accept or/and return a function
# closure occurs when a function is created within a function, as a result the inner function has access to data beyond its scope
# decorator is a function that is called with an @ that modifies the following function

def square(x):
    return x * x

print(list(map(square, numbers)))

def even(x):
    return x % 2 == 0

print(list(filter(even, numbers)))

from functools import reduce

def sum(x, y):
    return x + y

print(reduce(sum, numbers))

for i in countries:
    print(i)

for i in names:
    print(i)

for i in numbers:
    print(i)

cap_countries = list(map(lambda word: word.upper(), countries))
print(cap_countries)

squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

cap_names = list(map(lambda word: word.upper(), names))
print(cap_names)

print(list(filter(lambda word: "land" in word, countries)))

print(list(filter(lambda word: len(word) == 6, countries)))

print(list(filter(lambda word: len(word) >= 6, countries)))

print(list(filter(lambda word: word[0] == "E", countries)))

def get_string_lists(arr):
    return list(filter(lambda item: isinstance(item, "str"), arr))

print(reduce(sum, numbers))

def concat(x, y):
    if x.count(",") != 4:
        x += ", {}".format(y)
    else:
        x += ", and {} are north European countries".format(y)
    return x

print(reduce(concat, countries))