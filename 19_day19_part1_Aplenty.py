import re

START_WF_NAME = 'in'
ACCEPT = 'A'
REJECT = 'R'

def is_accepted(part, workflows):
    x, m, a, s  = part
    part_dict = {
        'x': x,
        'm': m,
        'a': a,
        's': s
    }
                
    current_wf_name = START_WF_NAME
    while current_wf_name not in [ACCEPT, REJECT]:
        current_wf = workflows[current_wf_name]
        for rule in current_wf:
            condition, success_condition_wf = rule
            if eval(condition, part_dict) == True:
                current_wf_name = success_condition_wf
                break
    
    return current_wf_name == ACCEPT


if __name__ == "__main__":
    input_file = "19_day19_input.txt"  # Specify the input file name

    try:
        # Attempt to open the file for reading
        with open(input_file, 'r') as file:
            # Read the entire file into a list of lines, removing trailing whitespace
            grid = file.read()
    except FileNotFoundError:
        # Handle the case where the file does not exist by printing an error message
        print("File not found. Please enter a valid file name.")
     
    wf_file, parts_file = grid.split('\n\n') 
    parts = set()
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')

    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        print(match)
        parts.add(tuple(map(int, match.groups())))
        print(parts)

    workflows = dict()

    rule_regex = re.compile('([a-zA-Z]+[<>]\d+):([a-zA-Z]+)')
    for line in wf_file.split('\n'):
        # Name
        index_of_curly= line.index('{')
        name = line[:index_of_curly]
        # Default rule
        rest_line = line[index_of_curly + 1:len(line)-1]
        default = rest_line.split(',')[-1]
        # Rules
        rules = []
        matches = re.findall(rule_regex, rest_line)
        for match in matches:
            rules.append((match[0], match[1]))
            # print(match[0], match[1], match[2], match[3])
        rules.append(('True', default))
        workflows[name] = rules


    print(workflows)
    total_sum = 0
    for part in parts:
        if is_accepted(part, workflows):
            total_sum += sum(part)

    print(total_sum)

