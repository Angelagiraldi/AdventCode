import re  # Import the regex module for pattern matching in strings

# Constants defining the starting workflow name and decision outcomes
START_WF_NAME = 'in'
ACCEPT = 'A'
REJECT = 'R'

def is_accepted(part, workflows):
    """
    Determines if a part is accepted or rejected based on defined workflows.
    
    Args:
        part (tuple): A tuple representing part attributes (x, m, a, s).
        workflows (dict): A dictionary mapping workflow names to their rules.
    
    Returns:
        bool: True if the part is accepted, False otherwise.
    """
    # Unpack part attributes into variables for easier access
    x, m, a, s  = part
    # Create a dictionary to evaluate conditions using part attributes
    part_dict = {'x': x, 'm': m, 'a': a, 's': s}
                
    # Initialize the current workflow name
    current_wf_name = START_WF_NAME
    # Loop until a decision (ACCEPT or REJECT) is reached
    while current_wf_name not in [ACCEPT, REJECT]:
        current_wf = workflows[current_wf_name]
        for rule in current_wf:
            condition, success_condition_wf = rule
            # Evaluate the condition; if True, move to the next workflow
            if eval(condition, part_dict):
                current_wf_name = success_condition_wf
                break
    
    return current_wf_name == ACCEPT


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
    # Define a regex pattern to extract part attributes
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')

    # Extract part attributes from the input data
    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        parts.add(tuple(map(int, match.groups())))

    # Initialize a dictionary to store workflows and their rules
    workflows = dict()

    # Define a regex pattern to extract workflow rules
    rule_regex = re.compile('([a-zA-Z]+[<>]\d+):([a-zA-Z]+)')
    for line in wf_file.split('\n'):
        index_of_curly = line.index('{')
        name = line[:index_of_curly]
        rest_line = line[index_of_curly + 1:len(line)-1]
        default = rest_line.split(',')[-1]
        rules = []
        matches = re.findall(rule_regex, rest_line)
        for match in matches:
            rules.append((match[0], match[1]))
        rules.append(('True', default))
        workflows[name] = rules

    # Calculate the total sum of attributes for accepted parts
    total_sum = 0
    for part in parts:
        if is_accepted(part, workflows):
            total_sum += sum(part)

    # Output the total sum of accepted parts
    print(total_sum)
