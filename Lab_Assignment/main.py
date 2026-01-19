# main.py

from shapes import *         # imports Circle and Rectangle
from shapes.triangle import Triangle  # explicit import for Triangle

# Create objects
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 4)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())
