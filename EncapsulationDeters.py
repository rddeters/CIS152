"""
Name : EncapsulationDeters.py
Author: River Deters
Created : 09/03/2023
Course: CIS 152 - Data Structure
Version: 2.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Description : A program that creates a Can class with multiple attributes and a __str__ method.
Input: Only input is object creation in the driver.
Ouput: __str__ method is the only output for applicable objects.
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code, either
    modified or unmodified. I have not given other fellow student(s) access to my program.
"""


class Can:
    def __init__(self, company='', content='', size=0.0, price=0.0):
        self._company = company
        self._content = content
        self._size = size
        self._price = price

    # Getters
    @property
    def company(self):
        return self._company

    @property
    def content(self):
        return self._content

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self._price

    # Setters
    @company.setter
    def company(self, company):
        self._company = company

    @content.setter
    def content(self, content):
        self._content = content

    @size.setter
    def size(self, size):
        self._size = size

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return f"Can Company={self._company}, Content={self._content}, Size={self._size}, Price={self._price:.2f}"


if __name__ == '__main__':
    # Big-O Complexity
    # The main method's complexity is O(1) because all operations are constant time operations.

    # Create Can 1 and print object
    soup_1 = Can("Field Day", "Black Beans", 13.0, 0.99)
    print(soup_1)

    # Create Can 2 and print object
    soup_2 = Can("S&W", "Peaches", 12.0, 2.39)
    print(soup_2)

    # Create Can 3 and print object
    soup_3 = Can("Green Giant", "Green Beans", 11.9, 1.79)
    print(soup_3)

    # Create Can 4 and print object
    soup_4 = Can("Del Monte", "Creamed Corn", 13.4, 2.49)
    print(soup_4)
