def process_file_content(line):
    """
    Processes a single line from the file.

    Args:
    line (str): A string from the file, typically a line.

    Returns:
    int: The total sum calculated from the line.
    """
    total_sum = 0  # Initialize total sum
    current_sum = 0  # Initialize current sum for each segment before a comma

    # Iterate over each character in the line
    for char in line:
        if char == ',':
            # If the character is a comma, add the current sum to the total sum
            total_sum += current_sum
            # Reset current sum for the next segment
            current_sum = 0
        else:
            # Update current sum based on the character's ASCII value
            # Multiply by 17 and take modulo 256 for each character
            current_sum = (current_sum + ord(char)) * 17 % 256

    return total_sum  # Return the total sum after processing the line

if __name__ == "__main__":
    input_file = "15_day15_input.txt"  # File name

    try:
        # Attempt to open the file
        with open(input_file, 'r') as file:
            # Read only the first line and remove any trailing newline/whitespace
            first_line = file.readline().strip()
            # Process the first line to calculate the result
            result = process_file_content(first_line)
            print(result)  # Print the result
    except FileNotFoundError:
        # If the file is not found, inform the user
        print("File not found. Please enter a valid file name.")
