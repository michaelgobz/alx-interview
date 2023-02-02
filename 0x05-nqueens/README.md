# n-queen-problem

# 0x05. N Queens

## Task
    The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

    Usage: nqueens N
    If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module

## Mathematical intuition
Uses the method of backtracking  
more  detials [here](https://en.wikipedia.org/wiki/Backtracking)

## Usage Example.
    julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

## limitaions

the algorithm performs bad with values of N > 20 
this is due to python runtime draw backs.


