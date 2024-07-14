# Day 7: 30 Days of python programming

it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(["X", "Boeing"])
print(it_companies)

it_companies.pop()
print(it_companies)

# remove will raise an error if the item does not exist within the set while discard will not

print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B.union(A)))

print(A.symmetric_difference(B))

del A
del B

ages = set(age)
print(f"Length of list: {len(age)}\nLength of set: {len(ages)}")

# A string is any text
# A list is an unorder, modifiable collection of items
# A tuple is an ordered, immutable collection of items
# A set is a collection of unordered distinct items

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
print(len(set(words)))