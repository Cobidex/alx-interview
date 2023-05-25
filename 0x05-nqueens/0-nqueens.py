#!/usr/bin/python3
"""Solving N Queens with Backtracking"""
import sys


def place_queens(n, row, board):
    """
    Method: place_queens - place n queens
            on an n by n board so that
            no queens are attacking each other.
    Parameters:
        - n: An integer that sets the board size and the number of queens.
        - row: The current row being considered for queen placement.
        - board: The current board configuration with queen placements.
    Return:
        All possible solutions to queen placement in the form of a
        list of lists.
    """
    for col in range(n):
        is_attacked = False
        for queen in board:
            if col == queen[1]:
                is_attacked = True
                break
            if row - col == queen[0] - queen[1]:
                is_attacked = True
                break
            if col - queen[1] == queen[0] - row:
                is_attacked = True
                break
        if not is_attacked:
            board.append([row, col])
            if row != n - 1:
                place_queens(n, row + 1, board)
            else:
                print(board)
            del board[-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    place_queens(n, 0, [])


if __name__ == '__main__':
    main()
