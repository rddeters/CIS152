"""
Name : DerivedClassRiverDeters.py
Author: River Deters
Created : 09/05/2023
Course: CIS 152 - Data Structure
Version: 1.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Description : A program that creates a Clothing class and two derived classes (Pants and Shirts)
    with multiple attributes and multiple methods: __str__, wash, pack, and hang.
Input: Only input is object creation in the driver.
Ouput: __str__, wash, hang, and pack methods for applicable objects .
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code,
    either modified or unmodified. I have not given other fellow student(s) access to my program.
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


class Pants(Clothing):
    def __init__(self, size='', color=''):
        super().__init__(size, color)

    def __str__(self):
        return f'pants size={self._size}, color={self.color}'

    def wash(self):
        return "Pants should be dry cleaned only"

    def hang(self):
        return "Hang pants rather than folding them to avoid wrinkles."


class Shirts(Clothing):
    def __init__(self, size='', color='', sleeves=''):
        super().__init__(size, color)
        self.size = size
        self._sleeves = sleeves

    @property
    def sleeves(self):
        return self._sleeves

    @sleeves.setter
    def sleeves(self, sleeves):
        if not sleeves == '':
            if sleeves in ["short", "long", "none"]:
                self._sleeves = sleeves
            else:
                raise ValueError("Sleeve type must be 'short', 'long', or 'none'")

    @Clothing.size.setter
    def size(self, size):
        if not size == '':
            if size in ["S", "M", "L"]:
                self._size = size
            else:
                raise ValueError("Size must be 'S', 'M', or 'L'")

    def __str__(self):
        return f'shirts size={self._size}, color={self.color}, sleeves={self._sleeves}'

    def wash(self):
        return "Shirts should be dry cleaned only"

    def hang(self):
        return "Hang shirts rather than folding them to avoid wrinkles."


if __name__ == '__main__':
    # Big-O Complexity
    # The main method's complexity is O(1) because all operations are constant time operations.

    # Pants class tester
    # Empty constructor
    pants_1 = Pants()
    print(pants_1)

    pants_2 = Pants("Medium", "Blue")
    print(pants_2)

    pants_1.size = "L"
    pants_1.color = "Black"
    print(pants_1)

    print(pants_1.hang())
    print(pants_1.wash())

    # Shirt class testers
    # Empty constructor
    shirts_1 = Shirts()
    print(shirts_1)

    # Constructor with acceptable inputs
    shirts_2 = Shirts("L", "Red", "long")
    print(shirts_2)

    print(shirts_2.hang())
    print(shirts_2.wash())

    # Expected error for shirt size
    shirts_1.size = "Medium"
    shirts_1.color = "Black"
    shirts_1.sleeves = "none"
    print(shirts_1)
