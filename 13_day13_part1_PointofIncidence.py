def are_elements_mirrored(lst, position):
    mirror = False
    if lst[position] == lst[position + 1]:
        for c in range(position+1):
            if ((position+c+1) <= len(lst)-1) and (position-c >=0):
                if lst[position-c]==lst[position+c+1]:
                    mirror = True
                else:
                    mirror = False
    return mirror
        
if __name__ == "__main__":
    # Set the input file name
    input_file = "13_day13_input.txt"
    
    try:
        # Try to open the specified file
        with open(input_file, 'r') as file:
            # Read the contents of the file into a list of strings
            file_content = file.readlines()
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found. Please enter a valid file name.")



    rows = {1:[]}
    columns = {1:[]}
    c = 1
    for line in file_content:
        if line.isspace():
            c += 1
            rows[c] = []
            columns[c] = []
        else:
            rows[c].append(line.replace('\n',''))
            for n, el in enumerate(line.replace('\n','')):
                if len(columns[c]) <= n:
                    columns[c].append(el)
                else:
                    columns[c][n] += el

    sum = 0
    for note in rows.keys():
        len_rows = len(rows[note])
        found_mirror_row = False
        for count in range(len_rows-1):    
            mirror = are_elements_mirrored(rows[note], count)
            if mirror == True:
                sum += 100*(count+1)
                found_mirror_row = True
                break
        if not found_mirror_row:
            len_column = len(columns[note])
            for count in range(len_column-1):
                mirror = are_elements_mirrored(columns[note], count)
                if mirror == True:
                    sum += (count+1)
                    break

    print(sum)


    pattern = []
    fh = open(input_file, 'r')
    total = 0    

    def find_reflection_line(first_axis, first_n):
        for i in range(1, len(pattern)):
            reflect_range = min(i, len(pattern) - i)
            for j in range(1, reflect_range + 1):
                if pattern[i - j] != pattern[i + j - 1]:
                    break
            else:
                if first_axis is None or first_axis != 'h' or first_n != i:
                    return 'h', i
        for i in range(1, len(pattern[0])):
            reflect_range = min(i, len(pattern[0]) - i)
            for j in range(1, reflect_range + 1):
                if [pattern[k][i - j] for k in range(len(pattern))] != [pattern[k][i + j - 1] for k in range(len(pattern))]:
                    break
            else:
                if first_axis is None or first_axis != 'v' or first_n != i:
                    return 'v', i
        return None, None

    while True:
        line = fh.readline()
        if line == '\n' or line == '':
            axis, n = find_reflection_line(None, None)
            for y, row in enumerate(pattern):
                for x, c in enumerate(row):
                    pattern[y][x] = '.' if c == '#' else '#'
                    new_axis, new_n = find_reflection_line(axis, n)
                    if new_axis is not None:
                        total += 100 * new_n if new_axis == 'h' else new_n
                        break
                    pattern[y][x] = c
                else:
                    continue
                break
            if line == '':
                print(total)
                quit()
            pattern = []
        else:
            pattern.append(list(line.strip()))
            

    