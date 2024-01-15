import numpy as np
from itertools import combinations

if __name__ == "__main__":

    input_file = "11_day11_input.txt"
    try:
        with open(input_file, 'r') as file:
            # Read the contents of the file
            file_content = file.readlines()
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")


    

    m = np.zeros((len(file_content), len(file_content[0]) - 1))
    for i, line in enumerate(file_content):
        m[i] = [char == "#" for char in line.strip()]

    h = m.sum(axis=0) == 0
    v = m.sum(axis=1) == 0

    nodes = []
    rp = 0
    for r in range(m.shape[0]):
        if v[r]:
            rp += 1
        cp = 0
        for c in range(m.shape[1]):
            if h[c]:
                cp += 1
            if m[r, c]:
                nodes.append((rp, cp))
            cp += 1
        rp += 1

    nodes = np.array(nodes)

    print(int(sum([np.linalg.norm(p[0] - p[1], 1) for p in combinations(nodes, 2)])))