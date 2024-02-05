# Check if this script is the main program and not being imported by another module
if __name__ == "__main__":
    input_file = "18_day18_input.txt"  # Specify the input file name

    try:
        # Attempt to open the file for reading
        with open(input_file, 'r') as file:
            # Read the entire file into a list of lines, removing trailing whitespace
            grid = file.read().splitlines()
    except FileNotFoundError:
        # Handle the case where the file does not exist by printing an error message
        print("File not found. Please enter a valid file name.")
        
    # Initialize the set of dug tiles with the starting position (0, 0)
    dug, x, y = {(0, 0)}, 0, 0
    # Define movement directions as a dictionary
    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    # Process each line of instructions from the file
    for line in grid:
        line = line.split()  # Split each line into direction and steps
        for i in range(int(line[1])):  # Repeat the action based on the number of steps
            # Update the current position based on the direction
            x, y = x + directions[line[0]][0], y + directions[line[0]][1]
            # Add the new position to the set of dug tiles
            dug.add((x, y))
        
    # Calculate the bounds of the grid area affected by digging
    min_x, min_y, max_x, max_y = min({tile[0] for tile in dug}), min({tile[1] for tile in dug}), max({tile[0] for tile in dug}), max({tile[1] for tile in dug})
    # Initialize sets to track old and new border tiles
    old_tiles = set()
    new_tiles = {(x, y) for y in range(min_y, max_y + 1) for x in [min_x, max_x] if (x, y) not in dug} | \
                {(x, y) for x in range(min_x, max_x + 1) for y in [min_y, max_y] if (x, y) not in dug}
    # Expand the border until no new tiles can be added
    while new_tiles:
        new_new_tiles = {(tile[0] + direction[0], tile[1] + direction[1]) 
                         for tile in new_tiles for direction in directions.values() 
                         if min_x <= tile[0] + direction[0] <= max_x and min_y <= tile[1] + direction[1] <= max_y 
                         and (tile[0] + direction[0], tile[1] + direction[1]) not in dug 
                         and (tile[0] + direction[0], tile[1] + direction[1]) not in old_tiles 
                         and (tile[0] + direction[0], tile[1] + direction[1]) not in new_tiles}
        old_tiles, new_tiles = old_tiles | new_tiles, new_new_tiles
    # Calculate and print the final result: total area minus the border tiles
    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(old_tiles))
