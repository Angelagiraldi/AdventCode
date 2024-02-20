from itertools import combinations
import sympy as sp


def solve(puzzle_input):
    first_three_hailstones = []
    for line in puzzle_input.split("\n")[:3]:
        nums = line.replace("@", ",").split(",")
        first_three_hailstones.append(tuple(map(int, nums)))

    unknowns = sp.symbols("x y z dx dy dz t1 t2 t3")
    x, y, z, dx, dy, dz, *time = unknowns

    equations = []  # build system of 9 equations with 9 unknowns
    for t, h in zip(time, first_three_hailstones):
        equations.append(sp.Eq(x + t * dx, h[0] + t * h[3]))
        equations.append(sp.Eq(y + t * dy, h[1] + t * h[4]))
        equations.append(sp.Eq(z + t * dz, h[2] + t * h[5]))

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])


if __name__ == "__main__":

    input_file = "24_day24_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, "r") as file:
            grid = file.read()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")

    print("Part 2:", solve(grid))
