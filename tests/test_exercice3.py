import pytest
from exercice3 import Shape, Rectangle, Circle, Square

def test_rectangle():
    rect = Rectangle(4, 5)
    assert rect.area() == 20
    assert rect.perimeter() == 18

def test_circle():
    circle = Circle(7)
    assert pytest.approx(circle.area(), 0.001) == 153.938
    assert pytest.approx(circle.perimeter(), 0.001) == 43.96

def test_square():
    square = Square(4)
    assert square.area() == 16
    assert square.perimeter() == 16

def test_inheritance():
    assert isinstance(Square(4), Rectangle)
    assert isinstance(Circle(7), Shape)
    assert isinstance(Rectangle(4, 5), Shape)
