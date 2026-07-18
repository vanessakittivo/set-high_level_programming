#!/usr/bin/python3
"""Solves the N queens problem."""

import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed."""
    for c in range(col):
        r = queens[c]

        if r == row:
            return False

        if abs(r - row) == abs(c - col):
            return False

    return True


def solve(queens, col, n):
    """Solve the puzzle using backtracking."""
    if col == n:
        solution = []
        for c in range(n):
            solution.append([c, queens[c]])
        print(solution)
        return

    for row in range(n):
        if is_safe(queens, row, col):
            queens[col] = row
            solve(queens, col + 1, n)


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = [-1] * n
    solve(queens, 0, n)


if __name__ == "__main__":
    main()
