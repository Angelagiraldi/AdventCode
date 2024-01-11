

def check_difference(current_line, result):

    lenght = len(current_line)
    new_line = []
    for count in range(1,lenght):
        new_line.append(int(current_line[count]) - int(current_line[count-1]))
    result += int(new_line[-1])

    all_zero = False
    for el in new_line:
        if el != 0:
            return check_difference(new_line, result)
        else:
            all_zero = True
            
    if all_zero:
        return result




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
        result = line[-1]
        res += check_difference(line, int(result))

    print(res)

