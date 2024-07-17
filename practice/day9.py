# Day 9: 30 Days of python programming

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

my_age = 23
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if your_age - my_age > 1:
        print(f"You are {your_age - my_age} years older than me.")
    else:
        print(f"You are {your_age - my_age} year older than me.")
elif your_age < my_age:
    if my_age - your_age > 1:
        print(f"You are {my_age - your_age} years younger than me.")
    else:
        print(f"You are {my_age - your_age} year younger than me.")
else:
    print("You are the same age as me.")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is eqal to {b}")

grade = int(input("Enter grade: "))
if grade >= 90:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50:
    print("D")
else:
    print("F")

autumn = ["September, October, November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
month = input("Enter month: ")
if month in autumn:
    print(f"{month} is in the autumn")
elif month in winter:
    print(f"{month} is in the winter")
elif month in spring:
    print(f"{month} is in the spring")
else:
    print(f"{month} is in the summer")

fruits = ["banana", "orange", "mango", "lemon"]
fruit = input("Enter fruit: ")
if fruit in fruits:
    print(f"{fruit} already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["Javascript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}
if "skills" in person.keys():
    print(person["skills"][len(person["skills"])//2])
if "skills" in person.keys():
    if "Python" in person["skills"]:
        print(f'{person["first_name"]} knows Python.')
    else:
        print(f'{person["first_name"]} does not know Python.')
if "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a fullstack developer")
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a backend developer")
elif len(person["skills"]) == 2 and "Javascript" in person["skills"] and "React" in person["skills"]:
    print("He is a frontend developer")
else:
    print("unknown title")

if person["is_married"] and person["country"] == "Finland":
    print(f'{person["first_name"]} {person["last_name"]} lives in Finland. He is married.')