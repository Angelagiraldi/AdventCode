input_file = "1_day1_input.txt"
try:
    # Open the file in read mode
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.read()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

def calculate_sum(file_content):
    total_sum = 0
    new_line = True
    last_number = 0

    for index, char in enumerate(file_content):
        if char.isdigit():
            
            digit = int(char)
            if new_line:
                total_sum += digit * 10
                new_line = False
                last_number = digit
            else:
                last_number = digit

            # Check if it's the last character in file_content and add the last digit to sum
            if index == len(file_content) - 1:
                total_sum += digit


        elif char == '\n':
            total_sum += last_number
            new_line = True
            last_number = 0

    return total_sum

print("Sum of all calibration values:", calculate_sum(file_content))


