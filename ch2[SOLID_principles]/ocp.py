import math
from typing import Protocol


class Shape(Protocol):
    def area(self) -> float:
        ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)
    
def calculate_area(shape: Shape) -> float:
    return shape.area()

if __name__ == "__main__":
    rect = Rectangle(12, 8)
    rect_area = calculate_area(rect)
    print(f"Rectangle area: {rect_area}")

    circ = Circle(6.5)
    circ_area = calculate_area(circ)
    print(f"Circle area: {circ_area:.2f}")