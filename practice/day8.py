# Day 8: 30 Days of python programming

dog = dict()

dog["name"] = "Cerberus"
dog["color"] = "black"
dog["breed"] = "German shepherd"
dog["legs"] = 4
dog["age"] = 2

student = {
"first_name": "Min",
"last_name": "Zhang",
"gender": "male",
"age": 23,
"marital_status": "single",
"skills": ["Python", "C++"],
"country": "USA",
"city": "El Paso",
"address": "123 St"}

print(len(student))

print(type(student.get("skills")))

student["skills"] += ["HTML", "SQL"]

print(student.keys())

print(student.values())

print(student.items())

student.popitem()
print(student.values())

del student