
input_file = "6_day6_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.read().split("\n")
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

print(file_content)
time_list = [int(time) for time in file_content[0].strip().split(": ")[1].split(" ") if time.isdigit()]
distance_list = [int(distance) for distance in file_content[1].strip().split(": ")[1].split(" ") if distance.isdigit()]

count = 1
for list, time in enumerate(time_list):

    print("Max distance:",distance_list[list])
    sum = 0
    for i in reversed(range(time+1)):
        print(i)
        print(i*(time-i))
        if i*(time-i)>distance_list[list]:
            sum += 1
        print(sum)
        print(" ")
    count *= sum

print(count)