class Circle:
    def __init__(self, radius: float):
        self._radius: float = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius can't be negative!")
        self._radius = value

if __name__ == "__main__":
    circle = Circle(10)
    print(f"Initial radius: {circle.radius}")

    circle.radius = 15
    print(f"New radius: {circle.radius}")    