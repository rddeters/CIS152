"""
Name : InterfacesDeters.py
Author: River Deters
Created : 09/05/2023
Course: CIS 152 - Data Structure
Version: 1.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Description : A program that creates a Measurements interface and two classes, Rectangle and Square,
    that use the interface.
Input: Only input is object creation in the driver.
Ouput: __str__, perimeter, and area methods.
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code,
    either modified or unmodified. I have not given other fellow student(s) access to my program.
"""


from abc import ABC, abstractmethod


class Measurements(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Measurements):
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __str__(self):
        return f'width={self.width}, height={self.height}'

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Square(Measurements):
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = side

    def __str__(self):
        return f'side={self.side}'

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side


if __name__ == '__main__':
    # Big-O Complexity
    # The main method's complexity is O(1) because all operations are constant time operations.

    # Driver/tester code for Rectangle class
    rectangle_1 = Rectangle(5, 4)
    print(rectangle_1)
    print(rectangle_1.perimeter())
    print(rectangle_1.area())

    # Driver/tester code for Square class
    square_1 = Square(6)
    print(square_1)
    print(square_1.perimeter())
    print(square_1.area())
