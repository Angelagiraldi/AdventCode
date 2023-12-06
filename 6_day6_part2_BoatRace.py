
input_file = "6_day6_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.read().split("\n")
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")

time = int(file_content[0].split(":")[1].replace(" ", ""))
dist = int(file_content[1].split(":")[1].replace(" ", ""))


sum = 0
for i in reversed(range(time+1)):
    if i*(time-i)>dist:
        sum += 1

print(sum)