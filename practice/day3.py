# Day 3: 30 Days of python programming

age = 23
height = 6.0
com = 1+1j

tri_base = float(input("Enter base: "))
tri_height = float(input("Enter height: "))
print("The area of the triangle is", 0.5 * tri_base * tri_height)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("The perimeter of the triangle is", a + b + c)

length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("The area of the rectangle is", length * width)
print("The perimeter of the rectangle is", 2 * (length + width))

pi = 3.14
radius = float(input("Enter radius: "))
print("The area of the circle is", pi * radius**2)
print("The circumference of the circle is", 2 * pi * radius)

slope = 2
x_int = 1
y_int = -2

m = (2 - 10) / (2 - 6)
distance = (2 - 6)**2 + (2 - 10)**2

print(slope == m)

x = -3 
y = x**2 + 6 * x + 9
print(y)

l1 = len("python")
l2 = len("dragon")
print(l1 != l2)

print("on" in "python" and "on" in "dragon")

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

print("on" not in "python" and "on" not in "dragon")

length = str(float(len("python")))

def even(val):
    if val % 2 == 0:
        return True
    else:
        return False
    
print(7//3 == int(2.7))

print(type("2.7") == type(10))

print(int(float("9.7")) == 10)

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

years = float(input("Enter the number of years you have lived: "))
seconds = 60 * 60 * 24 * 365 * years
print("You have lived for", seconds, "seconds.")

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)