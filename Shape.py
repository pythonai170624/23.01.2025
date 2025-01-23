import math


class Shape:
    def __init__(self, name: str):
        self.name = name

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
    def calc_hekef(self):
        perimeter: float = self.a + self.b + self.c
        return perimeter

    def calc_area(self):
        area: float = self.h * self.c / 2
        return area

    def __str__(self):
        return  (f"super: {super().__str__()} " +
                 f"[Triangle] a={self.a} b={self.b} c={self.c} h={self.h} " +
                 f"area={self.calc_area():.2f} \n  perimeter={self.calc_hekef()}")


class TriangleEqualSides (Triangle):
    def __init__(self, sides_len, h):
        super().__init__(sides_len, sides_len, sides_len, h, "equal_sides")

    # @override
    def calc_hekef(self):
        perimeter: float = self.a * 3
        return perimeter

    def __str__(self):
        return f"super: {super().__str__()} " + "[TriangleEqualSides]"

tr1 = Triangle(4.1, 4.7, 8.1, 3.5, name='triangle1')
eqs = TriangleEqualSides(6.99, 2.5)
print(tr1)
print(eqs)
