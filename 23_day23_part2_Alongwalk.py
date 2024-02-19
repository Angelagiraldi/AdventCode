import sys

sys.setrecursionlimit(10000)


def find_nodes():
    """
    Find the coordinates where you can take different paths, and
    the distance between each node
    """
    explored = set()
    nodes = {}
    queue = [(start,'v')]
    while len(queue) > 0:
        from_node, cur_dir = queue.pop()
        if (from_node,cur_dir) in explored:
            continue
        explored.add((from_node,cur_dir))
        cur_pos = from_node
        steps = 0
        while True:
            steps += 1
            cur_pos = adjust_pos(cur_pos, cur_dir)
            next_dirs = possible_dirs(cur_pos, cur_dir)
            if len(next_dirs) > 1 or cur_pos == end:
                to_node = cur_pos
                if from_node not in nodes: nodes[from_node] = []
                nodes[from_node].append((to_node,steps))
                if to_node not in nodes: nodes[to_node] = []
                nodes[to_node].append((from_node,steps))
                explored.add((to_node,reverse_dir(cur_dir)))
                for dir in next_dirs:
                    if (to_node,dir) not in explored:
                        queue.append((to_node,dir))
                break
            cur_dir = next_dirs[0]
    return nodes

def possible_dirs(cur_pos, cur_dir):
    next_dirs = []
    backtrack = reverse_dir(cur_dir)
    for dir in 'v>^<':
        if dir == backtrack:
            continue        # can't backtrack
        move_to = adjust_pos(cur_pos, dir)
        tile = map.get(move_to,'#')
        if tile != '#':
            next_dirs.append(dir)
    return next_dirs

def reverse_dir(cur_dir):
    idx = 'v>^<'.index(cur_dir)
    reverse_dir = '^<v>'[idx]
    return reverse_dir

def adjust_pos(coord, dir):
    x, y = coord
    adjust = {'>':(1,0), '<':(-1,0), 'v':(0,1), '^':(0,-1)}
    ax, ay = adjust[dir]
    x += ax
    y += ay
    return (x, y)


def take_a_hike():
    """
    Search the nodes to find the longest path from start to end, without
    passing a node twice
    """
    cache = {}
    longest_walk = 0
    visited = set()
    visited.add(start)
    queue = [(start,0,frozenset(visited))]
    while len(queue) > 0:
        cur_node, steps, visited = queue.pop()
        if cur_node == end:
            if steps > longest_walk:
                print(steps)
                longest_walk = steps
            continue
        if cache.get((cur_node,visited),-1) >= steps:
            continue    # already have same or longer path
        cache[(cur_node,visited)] = steps
        new_visited = set(visited)
        new_visited.add(cur_node)
        new_visited = frozenset(new_visited)
        for next_node, steps_to_node in nodes[cur_node]:
            if next_node in new_visited:
                continue    # in my set of visited nodes
            new_steps = steps + steps_to_node
            if cache.get((next_node,new_visited),0) >= new_steps:
                continue    # already have same or longer path
            queue.append((next_node,new_steps,new_visited))
    return longest_walk

if __name__ == "__main__":
    input_file = "23_day23_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, "r") as file:
            grid = file.read().splitlines()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")

    map = {}
    start = (1, 0)
    end = (len(grid[0]) - 2, len(grid) - 1)

    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            map[x, y] = ch

    nodes = find_nodes()

    longest_walk = take_a_hike()

    print()
    print("Longest walk:", longest_walk)
