import math

from sudoku import Sudoku


def generate(size):
    puzzle = Sudoku(size).difficulty(0.5).board
    for row in range(size ** 2):
        for cell in range(size ** 2):
            if puzzle[row][cell] is None:
                puzzle[row][cell] = 0
    return puzzle


def possible(puzzle, size, size_sq, y, x, num):
    for i in range(size_sq):
        if puzzle[y][i] == num:
            return False

    for i in range(size_sq):
        if puzzle[i][x] == num:
            return False

    x0 = (x//size) * size
    y0 = (y//size) * size
    for i in range(size):
        for j in range(size):
            if puzzle[y0 + i][x0 + j] == num:
                return False
    return True


def solve(puzzle, size, size_sq):
    for y in range(size_sq):
        for x in range(size_sq):
            if puzzle[y][x] == 0:
                for num in range(1, size_sq + 1):
                    if possible(puzzle, size, size_sq, y, x, num):
                        puzzle[y][x] = num
                        solve(puzzle, size, size_sq)
                        puzzle[y][x] = 0
                return False
    print_puzzle(puzzle)
    input("\nPRESS ENTER TO PRESENT ANOTHER SOLUTION")
    return True


def print_puzzle(puzzle):
    space_buffer = (len(puzzle) // 10) + 2
    for row in puzzle:
        string = ""
        for cell in row:
            string += str(cell).ljust(space_buffer)
        print("[ " + string + "]")


def main():
    size = int(input("INPUT PUZZLE SIZE : "))
    puzzle = generate(size)
    print("PUZZLE :")
    print_puzzle(puzzle)
    print("\nSOLUTIONS :")
    solve(puzzle, size, size**2)


if __name__ == '__main__':
    main()
