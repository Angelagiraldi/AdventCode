from collections import deque

def take_steps(step_limit):
    stepped_to = set()
    stepped_to.add(start)

    for s in range(step_limit):
        stepped_to = take_a_step(stepped_to)

    #print_garden(stepped_to)

    plots = len(stepped_to)
    return plots


def take_a_step(from_steps):
    to_steps = set()
    for pos in from_steps:
        for dir in 'NWES':
            new_pos = adjust_pos(pos, dir)
            if new_pos not in garden:
                continue
            if garden[new_pos] == '#':      # rock
                continue
            to_steps.add(new_pos)
    return to_steps

def adjust_pos(coord, dir):
    x, y = coord
    adjust = {'E':(1,0), 'W':(-1,0), 'S':(0,1), 'N':(0,-1)}
    ax, ay = adjust[dir]
    x += ax
    y += ay
    return (x, y)


def print_garden(stepped_to):
    for y in range(y_len):
        line = ''
        for x in range(x_len):
            ch = garden[(x,y)]
            if (x,y) in stepped_to:
                ch = 'O'
            line += ch
        print(line)
    return



if __name__ == "__main__":
    input_file = "21_day21_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, 'r') as file:
            grid = file.read().splitlines()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")

    garden = {}

    x_len = len(grid[0])
    y_len = len(grid)

    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            garden[(x,y)] = ch
            if ch == 'S':
                start = (x,y)

    plots = take_steps(64)

    print('Plots reached: ', plots)