# Day 6: 30 Days of python programming

t = tuple()

brother = ("David", "Joel")
sister = ("Kelly", "Kaylee")

siblings = brother + sister
print(siblings)

print(len(siblings))

family_members = siblings + ("Dad", "Mom")
print(family_members)

siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

fruits = ("apple", "oranges", "banana")
vegetables = ("onion", "potato", "carrots")
animal_prod = ("milk", "butter", "meat")
food_stuff_tp = fruits + vegetables + animal_prod
print(food_stuff_tp)

print(list(food_stuff_tp))

if len(food_stuff_tp)%2 == 1:
    print(food_stuff_tp[len(food_stuff_tp)//2])
else:
    print((food_stuff_tp[(len(food_stuff_tp)//2)-1], food_stuff_tp[len(food_stuff_tp)//2]))

print(food_stuff_tp[:3] + food_stuff_tp[-3:])

del food_stuff_tp

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("Estonia" in nordic_countries)

print("Iceland" in nordic_countries)