def aoc_hash(s):
    """
    Calculates a custom hash value for a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The hash value.
    """
    v = 0
    for char in s:
        v += ord(char)  # Add ASCII value of the character
        v *= 17         # Multiply by 17
        v %= 256        # Take modulo 256
    return v

if __name__ == "__main__":
    input_file = "15_day15_input.txt"

    try:
        # Open the file and read the first line
        with open(input_file, 'r') as file:
            first_line = file.readline().strip()
    except FileNotFoundError:
        # If the file is not found, print an error message
        print("File not found. Please enter a valid file name.")
        exit()

    # Initialize a list of 256 empty lists to represent boxes
    boxes = [[] for _ in range(256)]

    # Process each step in the first line of the file
    for step in first_line.split(','):
        operation = step.find('-')

        # Check if the step is a removal operation
        if step[-1] == '-':
            label = step[:-1]
            box = aoc_hash(label)
            # Remove the item with the matching label from the box
            for n, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box].pop(n)
                    break
        else:
            # Otherwise, it's an addition or update operation
            operation = step.find('=')
            label = step[:operation]
            box = boxes[aoc_hash(label)]
            focal_length = int(step[operation + 1:])
            # Update or add the item in the box
            for n, lens in enumerate(box):
                if lens[0] == label:
                    box[n] = (label, focal_length)
                    break
            else:
                box.append((label, focal_length))

    # Calculate and print the final sum
    total_sum = sum([(n + 1) * (m + 1) * lens[1] for n, box in enumerate(boxes) for m, lens in enumerate(box)])
    print(total_sum)
