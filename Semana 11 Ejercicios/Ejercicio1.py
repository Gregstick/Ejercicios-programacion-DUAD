import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = math.pi * (self.radius ** 2)
        print(f"El área del círculo es  {area}")


circle_1 = Circle(4)
circle_1.get_area()
circle_2 = Circle(8)
circle_2.get_area()