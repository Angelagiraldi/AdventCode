
input_file = "5_day5_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.read().split("\n\n")
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")


def get(depth, seed):

    for source,source_lenght,destination in map_ranges[depth]:
        if source <= seed < source_lenght:
            new = seed - source + destination
            return new if depth == 6 else get(depth + 1, new)
        
    return seed if depth == 6 else get(depth + 1, seed)



seeds = [int(seed) for seed in file_content[0].split(": ")[1].split()]
maps = [[[int(map) for map in num.split()] 
    for num in line.split(":\n")[1].splitlines()]
    for line in file_content[1:]
]
map_ranges = [[] for _ in range(7)]

for depth, map in enumerate(maps):
    for destination, source, lenght in map:
        map_ranges[depth].append([source, source + lenght, destination])

print(min([get(0, seed) for seed in seeds]))