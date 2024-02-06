import re  # Import the regex module for pattern matching in strings

# Constants defining the starting workflow name and decision outcomes
START_WF = 'in'

ACCEPT = 'A'
REJECT = 'R'

GREATER = ">"
LESS = "<"

'''
    IDEA:
        Rule1;                      true_range_r1
        !Rule1 & Rule2              false_range_r1 ∩ true_range_r2
        !Rule1 & !Rule2 & Rule3     false_range_r1 ∩ false_range_r2 ∩ true_range_r3
        ....
'''

def calculate_ranges_product(ranges):
    product = 1
    for start, end in ranges.values():
        product *= end - start + 1
    return product

def get_accepted_comb_number(ranges, wf_name,workflows):
    # BASE CASE (1)
    if wf_name == REJECT:
        return 0
    # BASE CASE (2)
    if wf_name == ACCEPT: 
        return calculate_ranges_product(ranges)

    rules, default = workflows[wf_name] # rules: list of rules; default: default workflow name

    total = 0
    is_condition_impossible = False
    for var, symb, num, target in rules:
        start, end = ranges[var]
        # Calculate the range for the true and false condition
        if symb == LESS:
            rule_true_range = (start, num-1)
            rule_false_range = (num, end)
        else: # symb == GREATER:
            rule_true_range = (num + 1, end)
            rule_false_range = (start, num)
        
        if rule_true_range[0] <= rule_true_range[1]:
            ranges_copy = dict(ranges)
            ranges_copy[var] = rule_true_range
            total += get_accepted_comb_number(ranges_copy, target, workflows)

        if rule_false_range[0] <= rule_false_range[1]:
            ranges = dict(ranges)
            ranges[var] = rule_false_range
        else:
            # Impossible Condition 
            is_condition_impossible = True
            break

    if not is_condition_impossible:
        total += get_accepted_comb_number(ranges, default, workflows)
    
    return total



if __name__ == "__main__":
    # Specify the input file name
    input_file = "19_day19_input.txt"  

    try:
        # Attempt to open and read the input file
        with open(input_file, 'r') as file:
            grid = file.read()
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
     
    # Split the input data into workflow definitions and parts to be checked
    wf_file, parts_file = grid.split('\n\n') 
    parts = set()
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        parts.add(tuple(map(int, match.groups())))

    # Initialize a dictionary to store workflows and their rules
    workflows = dict()

    # Define a regex pattern to extract workflow rules
    rule_regex = re.compile('([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
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
            rules.append((match[0], match[1], int(match[2]), match[3]))
            # print(match[0], match[1], match[2], match[3])
        workflows[name] = (rules, default)


    ranges_dict_0 = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    print(get_accepted_comb_number(ranges_dict_0, START_WF, workflows))