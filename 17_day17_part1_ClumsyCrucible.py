import numpy as np
import queue
from queue import PriorityQueue

def navigate(grid, minval=1, maxval=3):
    q = PriorityQueue()
    max_y, max_x = (v - 1 for v in grid.shape)
    goal = max_y, max_x
    q.put((0, (0, 0, 0)))
    q.put((0, (0, 0, 1)))
    seen = set()

    while q:
        cost, (y, x, direction) = q.get()
        if (y, x) == goal:
            break
        if (y, x, direction) in seen:
            continue
        seen.add((y, x, direction))
        original_cost = cost
        for s in [-1, 1]:
            cost = original_cost
            new_y, new_x = y, x
            for i in range(1, maxval + 1):
                if direction == 1:
                    new_x = x + i * s
                else:
                    new_y = y + i * s
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                cost += grid[new_y, new_x]
                if ((new_y, new_x, 1 - direction)) in seen:
                    continue
                if i >= minval:
                    q.put((cost, (new_y, new_x, 1 - direction)))
    return cost

if __name__ == "__main__":
    input_file = "17_day17_input.txt"  # File name

    try:
        # Attempt to open the file
        with open(input_file, 'r') as file:
            # Read only the first line and remove any trailing newline/whitespace
            grid = file.read().splitlines()
            # Process the first line to calculate the result
    except FileNotFoundError:
        # If the file is not found, inform the user
        print("File not found. Please enter a valid file name.")

    grid = np.array([[int(char) for char in line.strip()] for line in grid])

    print(navigate(grid))
