
input_file = '6_day6_input.txt'

try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.read().split("\n\n")
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

time_list = [int(time) for file_content[0].split(": ")[1].split(" ")]
distance_list = [int(distance) for file_content[1].split(": ")[1].split(" ")]

print(time_list)