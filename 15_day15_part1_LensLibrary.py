def process_file_content(line):
    total_sum = 0
    current_sum = 0

    for char in line:
        if char == ',':
            total_sum += current_sum
            current_sum = 0
        else:
            current_sum = (current_sum + ord(char)) * 17 % 256

    return total_sum

if __name__ == "__main__":
    input_file = "15_day15_input.txt"

    try:
        with open(input_file, 'r') as file:
            first_line = file.readline().strip()
            result = process_file_content(first_line)
            print(result)
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")