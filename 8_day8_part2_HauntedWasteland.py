import math
if __name__ == "__main__":

    input_file = "8_day8_input.txt"
    try:
        with open(input_file, 'r') as file:
            # Read the contents of the file
            file_content = file.readlines()
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

    instructions = file_content[0].replace('R', '1').replace('L', '0').strip()

    nodes = {} 
    for line in file_content[2::]:
        current = line.split('=')[0].replace(' ','').replace('\n','')
        nodes[current] = []
        positions = line.split('=')[1].replace(' ','').replace('\n','')
        next_positions = [x.strip() for x in positions[positions.find('(') + 1:positions.find(')')].split(',')]
        nodes[current] = next_positions
    
    a_nodes, cycles = [n for n in nodes.keys() if n.endswith("A")], []

    print(a_nodes)

    for n in a_nodes:
        not_arrived = True 
        count = 0   
        current_position = n 
        while not_arrived:
            current_position = nodes[current_position][int(instructions[count%len(instructions)])]
            count += 1
            if current_position.endswith('Z'):
                not_arrived = False    
        cycles.append(count)

    print(math.lcm(*cycles))
