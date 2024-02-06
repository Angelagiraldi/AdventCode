import re  # Import the regex module for pattern matching in strings.

# Constants defining the starting workflow name and decision outcomes.
START_WF = 'in'
ACCEPT = 'A'
REJECT = 'R'
GREATER = ">"
LESS = "<"

# This script calculates the number of acceptable combinations based on workflows and rules defined in an input file.

def calculate_ranges_product(ranges):
    """
    Calculates the product of the ranges for each variable.
    
    Args:
        ranges (dict): A dictionary where keys are variable names and values are tuples representing ranges (start, end).
    
    Returns:
        int: The product of the ranges, indicating the total number of combinations within these ranges.
    """
    product = 1
    for start, end in ranges.values():
        product *= end - start + 1  # Calculate the number of values in each range and multiply them together.
    return product

def get_accepted_comb_number(ranges, wf_name, workflows):
    """
    Recursively calculates the number of accepted combinations based on the current workflow.
    
    Args:
        ranges (dict): The current ranges for each variable.
        wf_name (str): The current workflow name.
        workflows (dict): A dictionary of all workflows and their rules.
    
    Returns:
        int: The number of combinations that are accepted by this workflow.
    """
    # Base case 1: if the workflow results in rejection, return 0 as no combinations are accepted.
    if wf_name == REJECT:
        return 0
    # Base case 2: if the workflow results in acceptance, calculate and return the product of the ranges.
    if wf_name == ACCEPT:
        return calculate_ranges_product(ranges)

    rules, default = workflows[wf_name]  # Extract rules and the default workflow for the current workflow.
    total = 0
    is_condition_impossible = False  # Flag to track if we encounter an impossible condition (no valid range).

    for var, symb, num, target in rules:
        start, end = ranges[var]  # Get the current range for the variable.
        # Adjust the range based on the rule's symbol and number.
        if symb == LESS:
            rule_true_range = (start, num - 1)
            rule_false_range = (num, end)
        else:  # symb == GREATER
            rule_true_range = (num + 1, end)
            rule_false_range = (start, num)
        
        # If the true range is valid, recursively calculate combinations for it.
        if rule_true_range[0] <= rule_true_range[1]:
            ranges_copy = dict(ranges)
            ranges_copy[var] = rule_true_range
            total += get_accepted_comb_number(ranges_copy, target, workflows)

        # Adjust the current ranges based on the false condition.
        if rule_false_range[0] <= rule_false_range[1]:
            ranges = dict(ranges)
            ranges[var] = rule_false_range
        else:
            is_condition_impossible = True  # Mark condition as impossible and break the loop.
            break

    # If no impossible condition was encountered, add combinations for the default workflow.
    if not is_condition_impossible:
        total += get_accepted_comb_number(ranges, default, workflows)
    
    return total  # Return the total number of accepted combinations.

if __name__ == "__main__":
    input_file = "19_day19_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, 'r') as file:
            grid = file.read()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")
     
    # Split the input data into workflow definitions and parts to be checked.
    wf_file, parts_file = grid.split('\n\n') 
    parts = set()
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    # Extract part attributes using regex.
    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        parts.add(tuple(map(int, match.groups())))

    # Initialize a dictionary to store workflows and their rules.
    workflows = dict()
    rule_regex = re.compile('([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
    for line in wf_file.split('\n'):
        index_of_curly = line.index('{')
        name = line[:index_of_curly]
        rest_line = line[index_of_curly + 1:len(line)-1]
        default = rest_line.split(',')[-1]
        rules = []
        # Extract rules using regex.
        matches = re.findall(rule_regex, rest_line)
        for match in matches:
            rules.append((match[0], match[1], int(match[2]), match[3]))
        workflows[name] = (rules, default)

    # Initialize the ranges for each variable.
    ranges_dict_0 = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    # Calculate and print the total number of accepted combinations.
    print(get_accepted_comb_number(ranges_dict_0, START_WF, workflows))
