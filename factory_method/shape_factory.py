'''
Create a simple Shape Factory that can create different geometric shapes.

Requirements:
- Create an abstract Shape class with an abstract method `area()` and `perimeter()`
- Implement concrete classes: Circle, Rectangle, and Square
- Create a ShapeFactory class with a static method `create_shape(shape_type, **kwargs)`
- The factory should accept the following parameters:
  - "circle" with radius
  - "rectangle" with width and height  
  - "square" with side
- Handle invalid shape types by raising a ValueError

Example usage:
```python
circle = ShapeFactory.create_shape("circle", radius=5)
rectangle = ShapeFactory.create_shape("rectangle", width=4, height=6)
square = ShapeFactory.create_shape("square", side=3)

print(f"Circle area: {circle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
```
Expected output:
Circle area: 78.54
Rectangle perimeter: 20
'''
from abc import ABC, abstractmethod

# Shape interface Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete classes
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side*self.side

    def perimeter(self):
        return 4*self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*self.width + 2*self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)

    def perimeter(self):
        return 2*3.14*self.radius

# Factory class
class ShapeFactory:
    @staticmethod
    def create_shape(shape, **kwargs):
        if shape == "square":
            return Square(**kwargs)
        if shape == "rectangle":
            return Rectangle(**kwargs)
        if shape == "circle":
            return Circle(**kwargs)

if __name__ == "__main__":
    circle = ShapeFactory.create_shape("circle", radius=5)
    rectangle = ShapeFactory.create_shape("rectangle", width=4, height=6)
    square = ShapeFactory.create_shape("square", side=3)

    print(f"Circle area: {circle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")
    print(f"Square area:  {square.area()}")