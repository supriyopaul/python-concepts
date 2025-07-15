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