import collections as C

if __name__ == "__main__":
    input_file = "25_day25_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, "r") as file:
            grid = file.read().splitlines()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")

    G = C.defaultdict(set)

    for line in grid:
        u, *vs = line.replace(":", "").split()
        for v in vs:
            G[u].add(v)
            G[v].add(u)

    S = set(G)

    count = lambda v: len(G[v] - S)

    while sum(map(count, S)) != 3:
        S.remove(max(S, key=count))

    print(len(S) * len(set(G) - S))
