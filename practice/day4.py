string = ["Thirty", "Days", "Of", "Python"]
print("".join(string))

string = ["Coding", "For", "All"]
print("".join(string))

string = "Coding For All"
company = string[0]

print(company)

print(len(company))

print(string.upper())

print(string.lower())

print(string.capitalize())

print(string.title())

print(string.swapcase())

print(string[:6])

print(string.index("Coding"))
print(string.find("Coding"))

print(string.replace("Coding", "Python"))

string = "Python for Everyone"
print(string.replace("Everyone", "All"))

string = "Coding For All"
print(string.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

print(string[0])

print(string[-1])

print(string[10])

string = "Python For Everyone"
string = string.split()
print(string[0][0] + string[1][0] + string[2][0])

string = "Coding For All"
print(string.index("C"))

print(string.index("F"))

string = "Coding For All People"
print(string.rindex("l"))

sentence = "You cannot end a sentence with becasue because because is a conjunction"
print(sentence.find("because"))

print(sentence.rindex("because"))

print(sentence[sentence.find("because"):sentence.rindex("because")+7])

string = "Coding For All"
print(string.startswith("Coding"))

print(string.endswith("coding"))

string = "   Coding For All      "
print(string.strip())

print("thirty_days_of_python".isidentifier())

libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(libs))

sentences = "I am enjoying this challenge. \nI just wonder what is next."
print(sentences.split("\n"))

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius**2
print(f"The area of a circle with radius {radius} is {area} meters square.")

val1 = 8
val2 = 6
print(f"{val1} + {val2} = {val1 + val2}")
print(f"{val1} - {val2} = {val1 - val2}")
print(f"{val1} * {val2} = {val1 * val2}")
print(f"{val1} / {val2} = {val1 / val2:.2f}")
print(f"{val1} % {val2} = {val1 % val2}")
print(f"{val1} // {val2} = {val1 // val2}")
print(f"{val1}**{val2} = {val1**val2}")