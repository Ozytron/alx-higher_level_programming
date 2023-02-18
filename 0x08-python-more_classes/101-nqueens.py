#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard."""
import sys


def init_chess_board(n):
    """initialize an N x N chessboard with space(" ") """
    chess_board = []
    [chess_board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in chess_board]
    return (chess_board)


def deepcopy_chess_board(chess_board):
    """deepcopy the chessboard"""
    if isinstance(chess_board, list):
        return list(map(deepcopy_chess_board, chess_board))
    return (chess_board)


def fetch_solution(chess_board):
    """fetches a solution by returning a list of list of the
    valid positions of N queens"""

    solution = []
    for r in range(len(chess_board)):
        for c in range(len(chess_board)):
            if chess_board[r][c] == "Q":
                solution.append([r, c])
                break
    return(solution)


def cross_out(chess_board, row, col):
    """
    all the positions on the board where a non-attacking queen
    cannot be placed are crossed out with "x".
    function args:
        chess_board (type = list): the current chessboard configuration.
        row (type = int): the row where a queen was last placed.
        col (type = int): the column where a queen was last placed.
    """

    # crossing out positions to the right
    for c in range(col + 1, len(chess_board)):
        chess_board[row][c] = "x"

    # crossing out positions to the left
    for c in range(col - 1, -1, -1):
        chess_board[row][c] = "x"

    # crossing out positions upwards
    for r in range(row - 1, -1, -1):
        chess_board[r][col] = "x"

    # crossing out positions downwards
    for r in range(row + 1, len(chess_board)):
        chess_board[r][col] = "x"

    # crossing out diagonal positions downwards stepping right.
    d = col + 1
    for r in range(row + 1, len(chess_board)):
        if d >= len(chess_board):
            break
        chess_board[r][d] = "x"
        d += 1

    # crossing out diagonal positions downwards stepping left.
    d = col - 1
    for r in range(row + 1, len(chess_board)):
        if d < 0:
            break
        chess_board[r][d] = "x"
        d -= 1

    # crossing out diagonal positions upwards stepping left.
    d = col - 1
    for r in range(row - 1, -1, -1):
        if d < 0:
            break
        chess_board[r][d] = "x"
        d -= 1

    # crossing out diagonal positions upwards stepping right.
    d = col + 1
    for r in range(row - 1, -1, -1):
        if d >= len(chess_board):
            break
        chess_board[r][d] = "x"
        d += 1


def solve_recursively(chess_board, row, queens, solutions):
    """
    this function solves recursively by placing queen "Q" at positions
    in the current chessboard to arrive at an arrangement where N queens
    are placed in a non-attacking position.
    function args:
        chess_board (type = list): the current working chessboard.
        row (type = int): the current working row.
        queens (type = int): the current number of queens placed on the board
        solutions (type = list): A list of lists of solutions.
    return:
        solutions
    """
    if queens == len(chess_board):
        """record the solution found"""
        solutions.append(fetch_solution(chess_board))
        return (solutions)

    for c in range(len(chess_board)):
        """
        solving for a valid arrangement of N non-attacking
        queens on the board.
        """
        if chess_board[row][c] == " ":
            temp_board = deepcopy_chess_board(chess_board)
            temp_board[row][c] = "Q"
            cross_out(temp_board, row, c)

            """The continue by solving recursively"""
            solutions = solve_recursively(temp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    chess_board = init_chess_board(int(sys.argv[1]))
    solutions = solve_recursively(chess_board, 0, 0, [])
    for soln in solutions:
        print(soln)
