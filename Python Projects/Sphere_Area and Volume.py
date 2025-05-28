import math

radius = float(input("Enter the radius of the Sphere: "))

area = 4 * math.pi * radius**2
volume = (4 / 3) * math.pi * radius**3

print(f"The Area of the Sphere is {round(area, 2)} m\u00b2")
print(f"The Volume of the Sphere is {round(volume, 2)} m\u00b3")
