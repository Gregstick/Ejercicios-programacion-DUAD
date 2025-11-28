from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self):
        self.radius = 0

    def set_radius(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self):
        self.side = 0

    def set_side(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_sides(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.base + self.height)

    def calculate_area(self):
        return self.base * self.height


circle = Circle()
circle.set_radius(5)

square = Square()
square.set_side(4)

rectangle = Rectangle()
rectangle.set_sides(6, 3)


print("El área del círculo es: ", circle.calculate_area(), "y el perímetro: ", circle.calculate_perimeter())
print("El área del cuadrado es: ", square.calculate_area(), "y el perímetro: ", square.calculate_perimeter())
print("El área del rectángulo es: ", rectangle.calculate_area(), "y el rectangle: ", rectangle.calculate_perimeter())