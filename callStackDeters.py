"""
Name : callStackDeters.py
Author: River Deters
Created : 09/12/2023
Course: CIS 152 - Data Structure
Version: 1.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Description : Create four methods that print "Entering methodX" and "Exiting methodX" with the X representing
    the method number (1 through 4).
Input: N/A
Ouput: Print statements in the main method and the 4 methods (Method1-Method4)
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code,
    either modified or unmodified. I have not given other fellow student(s) access to my program.
"""


def method1():
    print("In method 1")
    print("Exiting method 1")


def method2():
    print("In method 2")
    print("Exiting method 2")


def method3():
    print("In method 3")
    print("Exiting method 3")


def method4():
    print("In method 4")
    print("Exiting method 4")


if __name__ == '__main__':
    print("In main method")
    method2()
    method1()
    method4()
    method3()
    method4()
    method1()
    method3()
    method2()
    print("Exiting main method")
