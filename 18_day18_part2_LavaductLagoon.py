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
        
    h_lines, v_lines, x, y = [], [], 0, 0  # Initialize lists for storing line segments and starting coordinates
    
    # Process each line of instructions from the file
    for line in grid:
        line = line.split()  # Split each line into direction and steps
        n = int(line[2][2:7], 16)  # Convert steps from hexadecimal to integer
        direction = line[2][7]  # Extract direction from the instruction
        
        # Update horizontal or vertical lines based on direction, and adjust coordinates accordingly
        if direction == '0':  # Right
            h_lines.append((x, x + n, y))
            x += n
        elif direction == '1':  # Up
            v_lines.append((y, y + n, x))
            y += n
        elif direction == '2':  # Left
            h_lines.append((x - n, x, y))
            x -= n
        elif direction == '3':  # Down
            v_lines.append((y - n, y, x))
            y -= n
        
    # Create sorted lists of unique y-coordinates for horizontal lines and x-coordinates for vertical lines
    h_bars = sorted({h_line[2] for h_line in h_lines})
    v_bars = sorted({v_line[2] for v_line in v_lines})
    
    total = 0  # Initialize total metric to be calculated
    cells = []  # Initialize list to store processed cell information
    
    # Calculate the metric based on the grid formed by horizontal and vertical lines
    for y in range(len(h_bars) - 1):
        cell_row = []  # Initialize list to store row information
        h_bar_prev = h_bars[y]  # Previous horizontal bar position
        h_bar = h_bars[y + 1]  # Current horizontal bar position
        
        for x in range(len(v_bars) - 1):
            v_bar_left = False  # Flag to check if a vertical bar is on the left side
            # Check each vertical line to see if it intersects the current cell
            for v_line in v_lines:
                if h_bar_prev >= v_line[0] and h_bar <= v_line[1] and v_bars[x] == v_line[2]:
                    v_bar_left = True
                    break
            
            prev_in = False if (x == 0 or not cell_row[x - 1]) else True  # Check if the previous cell is included
            
            # Conditionally add cells based on the presence of vertical bars and previous cell inclusion
            if prev_in != v_bar_left:
                cell_row.append(True)
                # Calculate total based on the presence of vertical and horizontal bars
                total += (h_bar - h_bar_prev - 1) * (v_bars[x + 1] - v_bars[x] - 1)
                if prev_in:
                    total += h_bar - h_bar_prev - 1
                if y > 0 and cells[y - 1][x]:
                    total += v_bars[x + 1] - v_bars[x] - 1
                if prev_in and not v_bar_left and y > 0 and cells[y - 1][x] and cells[y - 1][x - 1]:
                    total += 1
            else:
                cell_row.append(False)
        cells.append(cell_row)
    
    # Print the final total metric, adjusted for the lengths of the lines and the number of lines
    print(total + sum([v_line[1] - v_line[0] + 1 for v_line in v_lines]) + sum([h_line[1] - h_line[0] + 1 for h_line in h_lines]) - len(v_lines) - len(h_lines))
