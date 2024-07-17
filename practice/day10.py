# Day 10: 30 Days of python programming

for i in range(11):
    pass
i = 0
while i <= 10:
    i += 1

for i in range(10,-1,-1):
    pass
i = 10
while i >= 0:
    i -= 1

string = ""
for i in range(7):
    string += "#"
    print(string)

for i in range(8):
    string = ""
    for j in range(8):
        string += "# "
    print(string)

for i in range(11):
    print(f"{i} x {i} = {i * i}")

items = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for item in items:
    print(item)

even = []
for i in range(101):
    if i % 2 == 0:
        even.append(i)
print(even)

odd = []
for i in range(101):
    if i % 2 != 0:
        odd.append(i)
print(odd)

sum = 0
for i in range(101):
    sum += i
print(f"The sum of all numers is {sum}.")

sum_odd = 0
sum_even = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")

fruits = ["banana", "orange", "mango", "lemon"]
rev_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    rev_fruits.append(fruits[i])
print(rev_fruits)