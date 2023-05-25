#!/usr/bin/python3
'''
contains the queens methods
'''

import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]

    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    # Base case: All queens have been placed
    if col >= N:
        solutions.append(board.copy())
        return

    # Recursive case: Try placing the queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1)
            board[row][col] = 0


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


# Main program
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(board, 0)

    # Print the solutions
    print_solutions(solutions)
