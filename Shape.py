import math

from abc import ABC, abstractmethod
from typing import override

class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calc_hekef(self):  # debt
        pass

    @abstractmethod
    def calc_area(self):  # debt
        pass

    def __str__(self):
        return "[Shape] name: " + self.name

class Triangle(Shape) :
    def __init__(self, a: float, b: float, c: float, h: float, name='triangle'):
        super().__init__(name)  # first action
        # self.name = "Triangle"  # wrong
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    # perimeter
    @override
    def calc_hekef(self):
        perimeter: float = self.a + self.b + self.c
        return perimeter

    @override
    def calc_area(self):
        area: float = self.h * self.c / 2
        return area

    def __str__(self):
        return  (f"super: {super().__str__()} " +
                 f"[Triangle] a={self.a} b={self.b} c={self.c} h={self.h} " +
                 f"\narea={self.calc_area():.2f} \n  perimeter={self.calc_hekef()}")


class TriangleEqualSides (Triangle):
    def __init__(self, sides_len, h):
        super().__init__(sides_len, sides_len, sides_len, h, "equal_sides")

    @override
    def calc_hekef(self):
        perimeter: float = self.a * 3
        return perimeter

    def __str__(self):
        return f"super: {super().__str__()} " + "[TriangleEqualSides]"

# malben
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('malben')
        self.width = width
        self.height = height

    # perimeter
    @override
    def calc_hekef(self):
        perimeter: float = 2 * (self.width + self.height)
        return perimeter

    @override
    def calc_area(self):
        area: float = self.width * self.height
        return area

    def __str__(self):
        return  (f"super: {super().__str__()} " +
                 f"[Rectangle] width={self.width} height={self.height}" +
                 f"area={self.calc_area():.2f} \n  perimeter={self.calc_hekef()}")

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    @override
    def calc_hekef(self):
        perimeter: float = self.width * 4
        return perimeter

    @override
    def calc_area(self):
        area: float = self.width ** 2
        return area

    def __str__(self):
        return f"super: {super().__str__()} [Square]"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius

    @override
    def calc_hekef(self):
        perimeter: float = 2 * math.pi * self.radius
        return perimeter

    @override
    def calc_area(self):
        area: float = math.pi * self.radius ** 2
        return area

    def __str__(self):
        return (f"super: {super().__str__()} " +
                f"[Circle] radius={self.radius} " +
                f"area={self.calc_area():.2f} \n  perimeter={self.calc_hekef()}")


tr1 = Triangle(4.1, 4.7, 8.1, 3.5, name='triangle1')
eqs = TriangleEqualSides(6.99, 2.5)
sq1 = Square(4.99)
circle1 = Circle(9.999)
print(circle1)
print(tr1)
print(eqs)
# s1 = Shape('amorphi')  # ERROR !!!!!!!!!!!!
# print(s1)

class Trapeziod(Shape):
    pass

#Trapeziod()
