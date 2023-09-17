"""
Name : SuperClassDeters.py
Author: River Deters
Created : 09/03/2023
Course: CIS 152 - Data Structure
Version: 2.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Description : A program that creates a Clothing class with multiple attributes and a __str__ method.
Input: Only input is object creation in the driver.
Ouput: __str__, wash, and pack methods for applicable objects .
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code, either
    modified or unmodified. I have not given other fellow student(s) access to my program.
"""


class Clothing:
    def __init__(self, size='', color=''):
        self._size = size
        self._color = color

    # Getter methods
    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color

    # Setter methods
    @size.setter
    def size(self, size):
        self._size = size

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'clothing size={self._size}, color={self.color}'

    def wash(self):
        return "Wash in cold water"

    def pack(self):
        return "Fold neatly and pack in a bag or suitcase"


if __name__ == '__main__':
    # Big-O Complexity
    # The main method's complexity is O(1) because all operations are constant time operations.

    # Tester/driver class or main method
    clothing_1 = Clothing()
    print(clothing_1)

    clothing_2 = Clothing("Medium", "Blue")
    print(clothing_2)

    clothing_1.size = "L"
    clothing_1.color = "Black"
    print(clothing_1)
