def backward_extrapolate_corrected(sequence):
    # Convert sequence to integers
    original_sequence = [int(x) for x in sequence]
    
    sequence = [int(x) for x in sequence]
    # Calculate the sequence of differences
    differences = []
    while not all(value == 0 for value in sequence):
        sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        differences.append(sequence.copy())



    # Reconstruct the original sequence

    extrapolated_value = 0
    for diff in reversed(differences):
        extrapolated_value = diff[0] - extrapolated_value


    extrapolated_value = original_sequence[0] - extrapolated_value
    return extrapolated_value




if __name__ == "__main__":

    input_file = "9_day9_input.txt"
    try:
        with open(input_file, 'r') as file:
            # Read the contents of the file
            file_content = file.readlines()
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

    res = 0
    for line in file_content:
        line = line.replace('\n','').split(' ')
        lenght = len(line)
        new_line = []
        result = line[0]
        res += backward_extrapolate_corrected(line)
        
    print(res)

