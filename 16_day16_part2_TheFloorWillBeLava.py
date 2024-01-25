if __name__ == "__main__":
    input_file = "16_day16_input.txt"  # File name

    try:
        # Attempt to open the file
        with open(input_file, 'r') as file:
            # Read only the first line and remove any trailing newline/whitespace
            grid = file.read().splitlines()
            # Process the first line to calculate the result
    except FileNotFoundError:
        # If the file is not found, inform the user
        print("File not found. Please enter a valid file name.")
        
    def calc_energized(grid, start):
        # (row, col, movement row, movement col)
        queue = [start]
        seen = set()

        while queue:
            row, col, drow, dcol = queue.pop(0)
            row += drow
            col += dcol

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue

            new_pos = grid[row][col]

            if (
                new_pos == "."
                or (new_pos == "-" and dcol != 0)
                or (new_pos == "|" and drow != 0)
            ):
                queue.append((row, col, drow, dcol))
                seen.add((row, col, drow, dcol))

            elif new_pos == "\\":
                drow, dcol = dcol, drow
                if (row, col, drow, dcol) not in seen:
                    queue.append((row, col, drow, dcol))
                    seen.add((row, col, drow, dcol))

            elif new_pos == "/":
                drow, dcol = -dcol, -drow
                if (row, col, drow, dcol) not in seen:
                    queue.append((row, col, drow, dcol))
                    seen.add((row, col, drow, dcol))

            else:
                for dr, dc in [(1, 0), (-1, 0)] if new_pos == "|" else [(0, 1), (0, -1)]:
                    if (row, col, dr, dc) not in seen:
                        queue.append((row, col, dr, dc))
                        seen.add((row, col, dr, dc))

        visited = {(row, col) for (row, col, _, _) in seen}

        return len(visited)


solution = 0
for row in range(len(grid)):
    solution = max(
        solution,
        calc_energized(grid, (row, -1, 0, 1)),
        calc_energized(grid, (row, len(grid), 0, -1)),
    )

for col in range(len(grid[0])):
    solution = max(
        solution,
        calc_energized(grid, (-1, col, 1, 0)),
        calc_energized(grid, (len(grid), col, -1, 0)),
    )

print(f"Solution: ", solution)
