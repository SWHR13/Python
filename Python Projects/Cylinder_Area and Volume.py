# A=2πrh+2πr2
# V = πr2h

import math

radius = float(input("Enter the radius of the Cylinder: "))
height = float(input("Enter the height of the Cylinder: "))

Area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
Volume = math.pi * radius**2 * height

print(f"The Area of the Cylinder is {round(Area, 2)} m\u00b2")


"""OR
    print("The Area of the Cylinder is " + str(round(Area, 2)) + " m\u00b2")
"""

print(f"The Volume of the Cylinder is {round(Volume, 2)} m\u00b3")
