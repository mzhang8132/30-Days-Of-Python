# Day 5: 30 Days of python programming

l = list()

l = [1, 2, 3, 4, 5]

print(len(l))

print(l[0], l[len(l)//2], l[-1])

mixed_data_types = ["Min", 23, 6, False, "USA"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

it_companies[-1] = "AWS"
print(it_companies)

it_companies.append("Amazon")
print(it_companies)

it_companies.insert(len(it_companies)//2, "X")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

print("#; ".join(it_companies))

print("Apple" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

print(it_companies[len(it_companies)//2])

it_companies.remove(it_companies[0])
print(it_companies)

it_companies.remove(it_companies[len(it_companies)//2])
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(full_stack.index("Redux") + 1, "SQL")
full_stack.insert(full_stack.index("Redux") + 1, "Python")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print("Min:", ages[0])

print("Max:", ages[-1])

median = ages[0]
if len(ages) % 2 == 0:
    median = (ages[len(ages)//2] + ages[(len(ages)//2) - 1]) / 2
else:
    median = ages[len(ages)//2]
print("Median:", median)

average = sum(ages) / len(ages)
print("Average:", average)

print("Range:", ages[-1] - ages[0])

diff_min = ages[0] - average
diff_max = ages[-1] - average
print(diff_min == diff_max)

countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
c1, c2, c3, *scandic = countries
print(c1, c2, c3, scandic)