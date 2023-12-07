
strenght = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

hands = []

def determine_type(cards):
    #ordering the 5 cards based on their reversed ASCII values: letters and then numbers
    cards = ''.join(sorted(cards, reverse=True,))
    
    #To check how many different labels are in the cards
    labels = []
    labels_size = 1
    
    #Use ordered first card label as reference
    current_card = cards[0]
    
    #Let's iterates through each character in the cards string 
    # starting from the second character 
    for card in cards[1::]:
        if card == current_card:
            labels_size += 1
        else:
            labels.append(labels_size)
            labels_size = 1
        current_card = card
    labels.append(labels_size)

    num_labels = len(labels)
    biggest_label = max(labels)

    if num_labels == 1:
        return 1
    elif num_labels == 2:
        if biggest_label == 4:
            return 2
        else:
            return 3
    elif num_labels == 3:
        if biggest_label == 3:
            return 4
        else:
            return 5
    elif num_labels == 4:
            return 6
    else:
        return 7

def custom_sort_key(item):
    try:
        label_indices = [strenght.index(char) for char in item[0]]
        return (item[2], *strenght)
    except ValueError:
        # Handle the case where a character is not found in labels list
        return (float('inf'),) * (len(item[0]) + 1)




if __name__ == "__main__":

    input_file = "7_day7_input.txt"
    try:
        with open(input_file, 'r') as file:
            # Read the contents of the file
            file_content = file.read().split("\n")
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

    for line in file_content:
        cards, bid = line.split()
        hand_type = determine_type(cards)
        hands.append((cards, bid, hand_type))
    
#    print(hands)

    hands = sorted(hands, key=custom_sort_key)
    hands = sorted(hands, reverse = True, 
                   key=lambda x: (x[2], strenght.index(x[0][0]), strenght.index(x[0][1]), strenght.index(x[0][2]), strenght.index(x[0][3]), strenght.index(x[0][4])))

    winnings = 0
    for rank, hand in enumerate(hands):
        winnings += int(hand[1]) * (rank + 1)
#        print(f"Hand: {hand} rank: {rank + 1} bid: {hand[1]}")

    print(f"Winnings: {winnings}")
