if __name__ == "__main__":
    # Set the input file name
    input_file = "12_day12_input.txt"
    try:
        # Try to open the specified file
        with open(input_file, 'r') as file:
            # Read the contents of the file into a list of strings
            file_content = file.readlines()
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found. Please enter a valid file name.")

    # Initialize a variable to store the total number of ways
    ways = 0
    # Iterate through each row in the file content
    for row in file_content:
        # Split the row into record and checksum
        record, checksum = row.split()
        # Convert checksum string to a list of integers
        checksum = [int(n) for n in checksum.split(',')]
        # Create a dictionary to store positions, initialized with the first position
        positions = {0: 1}

        # Iterate through each contiguous segment in the checksum
        for i, contiguous in enumerate(checksum):
            # Create a new dictionary to store updated positions
            new_positions = {}
            # Iterate through each position in the current positions
            for k, v in positions.items():
                # Iterate through possible starting positions in the record
                for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
                    # Check if the segment fits in the record without '#' characters
                    if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
                        # Check if it's the last segment or the next character is not '#'
                        if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) or (i < len(checksum) - 1 and n + contiguous < len(record) and record[n + contiguous] != '#'):
                            # Update the new positions dictionary
                            new_positions[n + contiguous + 1] = new_positions.get(n + contiguous + 1, 0) + v
                    # If '#' is encountered, break the loop
                    if record[n] == '#':
                        break
            # Update the positions dictionary with the new positions
            positions = new_positions

        # Sum the values in the positions dictionary and add to the total ways
        ways += sum(positions.values())

    # Print the total number of ways
    print(ways)