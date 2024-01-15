import numpy as np
from itertools import combinations

def parse(path):
    with open(path) as file:
        data = np.array([list(line.strip()) for line in file])

    return data


def solve(data, mult=1):
    mult = max(1, mult - 1)

    dots = data == "."
    rows = np.cumsum(np.all(dots, axis=1).astype(int) * mult)
    cols = np.cumsum(np.all(dots, axis=0).astype(int) * mult)

    rowd = np.arange(len(rows)) + rows
    cold = np.arange(len(cols)) + cols

    bity, bitx = np.where(data == "#")
    outx = np.abs(rowd[bity] - rowd[bity][:, np.newaxis])
    outy = np.abs(cold[bitx] - cold[bitx][:, np.newaxis])

    return np.triu(outx + outy).sum()



def solve_part2(data, mult=1000000):
    return solve(data, mult)


# Read input from a file

data = parse("11_day11_input.txt")

print(solve_part1(data))
print(solve_part2(data))