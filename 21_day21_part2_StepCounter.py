import re
from collections import defaultdict


def possible_points(point, garden_map):
    # Loop over all possible directions, and yield each possible new point
    # Check the remainder of the point axis' divided by 131 to continue moving outward infinitely for part 2
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for d in directions:
        new_point = (point[0] + d[0], point[1] + d[1])
        if garden_map[new_point[1] % 131][new_point[0] % 131] != '#':  # Make sure it wasn't a rock
            yield new_point

def bfs(point, garden_map, max_dist):
    # Use the Breadth first search to find the number of points hit each step, and return the dictionary with key of number of steps taken, 
    # and value of number of points hit
    tiles = defaultdict(int)
    visited = set()
    queue = [(point, 0)]
    while queue:  # End when the queue is empty
        curr_point, dist = queue.pop(0)
        if dist == (max_dist + 1) or curr_point in visited:  # Don't include points that have already been visited
            continue

        tiles[dist] += 1
        visited.add(curr_point)

        for next_point in possible_points(curr_point, garden_map):  # Loop over possible points and add to queue
            queue.append((next_point, (dist + 1)))
    return tiles

def calculate_possible_spots(start, garden_map, max_steps):
    # Get the output from bfs, and then return the sum of all potential stopping points in the tiles output based on even numbers
    tiles = bfs(start, garden_map, max_steps)
    return sum(amount for distance, amount in tiles.items() if distance % 2 == max_steps % 2)

def quad(y, n):
    # Use the quadratic formula to find the output at the large steps based on the first three data points
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * n**2) + (b * n) + c

def part2(parsed_data):
    # Calculate the first three data points for use in the quadratic formula, and then return the output of quad
    goal = 26501365
    size = len(parsed_data[1])
    edge = size // 2

    y = [calculate_possible_spots(*parsed_data, (edge + i * size)) for i in range(3)]
    
    return quad(y, ((goal - edge) // size))


if __name__ == "__main__":
    input_file = "21_day21_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, 'r') as file:
            grid = file.read().splitlines()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")

    for idx, line in enumerate(grid):
        start = re.search(r'S', line)
        if start is not None:
            start = (start.start(), idx)
            break
    data_list = [list(line) for line in grid]
    parsed_data = (start, data_list)

    print(part2(parsed_data))