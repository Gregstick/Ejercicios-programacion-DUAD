import math

class Circle:
    radius = 100
    
    def get_area(self):
        area = math.pi * (self.radius ** 2)
        print(f"El área del círculo es  {area}")


circle_1 = Circle()
circle_1.get_area()