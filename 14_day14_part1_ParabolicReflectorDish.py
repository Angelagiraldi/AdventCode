if __name__ == "__main__":
    # Set the input file name
    input_file = "14_day14_input.txt"
    
    try:
        # Try to open the specified file
        with open(input_file, 'r') as file:
            # Read the contents of the file into a list of strings
            file_content = file.readlines()
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found. Please enter a valid file name.")

    rows = []
    for row in file_content:
        rows.append(row.replace('\n',''))

    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != 'O':  # skip non-moving rocks
                continue
            obstacles_y = [y for y in range(y) if rows[y][x] in '#O']
            new_y = max(obstacles_y, default=-1) + 1
            if new_y != y:
                rows[y] = rows[y][:x] + '.' + rows[y][x+1:]
                rows[new_y] = rows[new_y][:x]+'O'+rows[new_y][x+1:]
    
    height = len(rows)
    load = sum(row.count('O') * (height - y) for y, row in enumerate(rows))

    print(load)