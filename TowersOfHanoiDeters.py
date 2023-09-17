"""
Name : TowersOfHanoiDeters.py
Author: River Deters
Created : 09/12/2023
Course: CIS 152 - Data Structure
Version: 1.0
OS: Windows 10
IDE: PyCharm 2022.3.1
Copyright : This is my own original work based on specifications issued by our instructor
Academic Honesty: I attest that this is my original work. I have not used unauthorized source code,
    either modified or unmodified. I have not given other fellow student(s) access to my program.

Recursion is where a function or method calls itself in the function. While a program can be broken
    into smaller parts, recursion can be used to make a program shorter and easier to read. There are
    multiple parts of a recursive function, a base case so it doesn't repeat infinitely, and the
    recursive case where the function calls itself. The base case is usually n < 0 or n == 0, where n
    is the value being inputted into the function. The recursive function typically will call itself in
    its definition, with the input being (n - 1) so its not repeating infinitely.

Recursion is used in this program, as the countMoves function/method is a recursive function. The goal
    for this program is to calculate the total number of moves it takes for a number of disks provided
    by a user. To calculate the number of moves, the disks need to move from the source peg to the
    auxiliary peg (countMoves(n-1) moves), the largest disk needs to move to the target peg (1 move),
    and then the rest of the disks need to move from the auxiliary peg to the target peg (countMoves(n-1)
    moves). It's much easier to use a recursive function to calculate the moves this way rather than
    breaking it down per move or step and calculating it that way.
"""


def countMoves(n):
    if n == 0:
        return 0
    return 2 * countMoves(n - 1) + 1


if __name__ == '__main__':
    disks = int(input('Please enter the number of disks: '))
    moves = countMoves(disks)
    print(str(disks) + ' disks requires ' + str(moves) + ' moves.')
