# Day 13: 30 Days of python programming

numbers = [-4, -3, -2, -1, 0, 2 , 4, 6]
non_postives = [i for i in numbers if i <= 0]
print(non_postives)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [j for i in list_of_lists for j in i[0]]
print(flattened)

tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
flattened = [[x.upper(), x.upper()[:3], y.upper()] for i in countries for (x, y) in i]
print(flattened)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
dictionary = [{"country": x, "city": y} for i in countries for (x, y) in i]
print(dictionary)

names = [[("Asabeneh", "Yetayeh")], [("David", "Smith")], [("Donald", "Trump")], [("Bill", "Gates")]]
strings = ["{} {}".format(x, y) for i in names for (x, y) in i]
print(strings)

slope = lambda x1, x2, y1, y2: (y1 - y2) / (x1 - x2)