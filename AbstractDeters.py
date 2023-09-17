"""
Name : AbstractDeters.py
Author: River Deters
Created : 09/05/2023
Course: CIS 152 - Data Structure
Version: 1.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Description : A program that creates a Cycle abstract class and a Bicycle subclass.
Input: Only input is object creation in the driver.
Ouput: __str__, ride, and stop methods.
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code,
    either modified or unmodified. I have not given other fellow student(s) access to my program.
"""

from abc import ABC, abstractmethod


class Cycle(ABC):
    def __init__(self, num_tires=0, num_flat=0):
        self._num_tires = num_tires
        self._num_flat = num_flat

    # Getter methods
    @property
    def num_tires(self):
        return self._num_tires

    @property
    def num_flat(self):
        return self._num_flat

    # Setter methods
    @num_tires.setter
    def num_tires(self, num_tires):
        self._num_tires = num_tires

    @num_flat.setter
    def num_flat(self, num_flat):
        self._num_flat = num_flat

    def __str__(self):
        return f'number_tires={self.num_tires}, number_flat_tires={self.num_flat}'

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Bicycle(Cycle):
    def __init__(self, num_tires=0, num_flat=0):
        super().__init__(num_tires, num_flat)

    def ride(self):
        return 'Pedal to begin riding the bicycle.'

    def stop(self):
        return 'Hold the brake on the handlebars or stop pedalling to stop the bicycle.'


if __name__ == '__main__':
    # Big-O Complexity
    # The main method's complexity is O(1) because all operations are constant time operations.

    # Driver/tester code for Bicycle class
    bike_1 = Bicycle(2, 0)
    print(bike_1)
    print(bike_1.ride())
    print(bike_1.stop())
