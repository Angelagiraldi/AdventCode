input_file = "1_day1_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

# Mapping of spelled-out numbers to their corresponding numerical values
word_to_digit = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
    'nine': '9'
}

total_sum = 0  # Initialize the total sum of calibration values

for line in file_content:
    line = line.strip()  # Remove leading/trailing whitespace and newline characters
    line_sum = 0  # Initialize the sum for the current line
    char_sequence = ''  # Initialize a sequence to capture alphabetic characters
    digit_sequence = []  # Initialize a sequence to capture digits
    print(line)
    # Iterate through each character in the line
    for char in line:
        if char.isalpha():
            char_sequence += char  # Collect sequential alphabetic characters
            
            # Check if the collected characters form a spelled-out number
            for dig in word_to_digit.keys():
                if dig in char_sequence:
                    digit = word_to_digit[dig]  # Get the corresponding numerical digit
                    digit_sequence.append(digit)  # Append the digit to the sequence
                    char_sequence = char_sequence[-1] # Keep only last character, for cases like eightwo to be considered as 82

        else:  # Assuming it's a numerical digit
            char_sequence = ''
            digit_sequence.append(char)  # Append numerical digit to the sequence
    
    print(digit_sequence)
    print(digit_sequence[0], digit_sequence[-1])
    # Calculate the calibration value based on the extracted first and last digits
    total_sum += int(digit_sequence[0]) * 10 + int(digit_sequence[-1])

print("Sum of all calibration values:", total_sum)