
input_file = "2_day2_input.txt"
try:
    with open(input_file, 'r') as file:
        # Read the contents of the file
        file_content = file.readlines()
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")






cube_counts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
possible_game_ids = []

def possible_game(game, cube_counts, possible_game_ids):
    game_info = game.split(': ')[1].split('; ')  # Split game info
    subsets = [subset.split(', ') for subset in game_info]  # Split subsets

    valid_game = True
    for subset in subsets:
        cube_info = {subset_part.split()[1]: int(subset_part.split()[0]) for subset_part in subset}
        for color, count in cube_info.items():
            if count > cube_counts[color]:
                valid_game = False
                break

    if valid_game:
        game_id = int(game.split(':')[0].split()[1])
        possible_game_ids.append(game_id)


# Split input into individual games
for games in file_content:
    possible_game(games, cube_counts, possible_game_ids)

print("Sum of IDs of possible games:", sum(possible_game_ids))


    
