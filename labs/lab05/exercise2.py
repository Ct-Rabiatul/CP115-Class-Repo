import math

print("This program will calculate area and circumference of circle")

radius = float(input("Enter the radius: " ))

area = math.pi * (radius * radius)
circumference = 2 * math.pi * radius

print()
print("Area: " + float(area))
print("Circumference: " + float(circumference))