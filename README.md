#⛄ 🎁 <span style="color:red;">AdventCode</span> 🎄 🤶

 🎅🦌❄️🕯️<span style="color:green;">Collection of my solutions in Python for the  [Code Advent Calendar 2023](https://adventofcode.com). </span> 🔔🎶🥛🍪
 

| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
| -- | -- | -- | -- | -- | 

Here the description of the challenges:

##--Day 1: Trebuchet?! --
####PART 1
The task at hand is to *decipher a calibration document* provided by the Elves, where each line of text contains specific calibration values. The goal is to extract these values by taking the first digit and the last digit of each line and combining them to form a two-digit number. For instance, from the line "1abc2," the calibration value would be 12 (using the first and last digits in that order). This process needs to be applied to all lines in the document, and the sum of all the extracted calibration values should be calculated and provided as the final answer.
####PART 2
The new task requires extracting the real first and last digits, which may be represented as spelled-out numbers ("one" to "nine"), from each line in the calibration document. The goal is to identify the actual numerical values represented by words and then combine the first and last digits (either numerical or spelled-out) of each line to form two-digit numbers. Finally, the task is to calculate the sum of all these extracted calibration values.

##--Day 2: Cube Conundrum  --
####PART 1

The task involves playing a game on Snow Island where an Elf presents a bag filled with red, green, and blue cubes. Throughout several games, the Elf reveals subsets of these cubes from the bag, and the objective is to determine which games would have been possible if the bag initially contained 12 red cubes, 13 green cubes, and 14 blue cubes.
To accomplish this, the information provided includes game IDs along with subsets of cubes revealed in each game. By comparing the revealed subsets against the specified cube counts, the task is to identify games where no subset exceeds the given cube limits. The final step involves summing up the IDs of these possible games as the solution to the task.

####PART 2
The task is to determine, for each game played on Snow Island, the minimum number of cubes of each color that must have been in the bag to make the game possible. The Elf specifies that the fewest cubes of each color are needed to ensure the game's feasibility.
To achieve this, we're given the same set of example games. For instance, in Game 1, the minimum set of cubes consisted of 4 red, 2 green, and 6 blue cubes. The key is to ascertain the minimum number of cubes for each color without which the game would have been impossible to play.
The calculation of this minimum set of cubes involves identifying the lowest count for each color within each game scenario. The power of a set of cubes is determined by multiplying the counts of red, green, and blue cubes together. The task requires computing these minimum sets for each game and calculating the sum of the powers derived from these sets across all the games to obtain the final solution.

##--Day 3: Gear Ratios  --
####PART 1
This challenge involves an encounter with an Elf at a gondola lift station. The gondolas are not functioning due to a missing engine part. The Elf, surprised by your arrival, explains that any number adjacent to a symbol (including diagonally adjacent numbers) within the engine schematic constitutes a "part number." Your task is to add up all these part numbers in the engine schematic to identify the missing part. However, periods (.) within the schematic do not count as symbols for this purpose.

####PART 2
Despite fixing the missing part, the gondola hasn't left the station due to an unresolved issue. The problem lies with certain symbols denoted as '*' in the engine schematic. A 'gear' is any '*' symbol that is adjacent to exactly two 'part numbers' (as defined previously). The gear ratio of a gear is the result of multiplying the two adjacent part numbers together.
The task requires finding and calculating the gear ratios of all gears present in the engine schematic. Each gear's ratio is obtained by multiplying the two adjacent part numbers connected to the gear. The goal is to sum up all the gear ratios to help identify the problematic gear that needs replacement in the engine.


##--- Day 4: Scratchcards ---

The gondola takes you up. Strangely, though, the ground doesn't seem to be coming with you; you're not climbing a mountain. As the circle of Snow Island recedes below you, an entire new landmass suddenly appears above you! The gondola carries you to the surface of the new island and lurches into the station.

As you exit the gondola, the first thing you notice is that the air here is much warmer than it was on Snow Island. It's also quite humid. Is this where the water source is?

The next thing you notice is an Elf sitting on the floor across the station in what seems to be a pile of colorful square cards.

"Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?" You ask about water sources.

"I'm not sure; I just operate the gondola lift. That does sound like something we'd have, though - this is Island Island, after all! I bet the gardener would know. He's on a different island, though - er, the small kind surrounded by water, not the floating kind. We really need to come up with a better naming scheme. Tell you what: if you can help me with something quick, I'll let you borrow my boat and you can go visit the gardener. I got all these scratchcards as a gift, but I can't figure out what I've won."

The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of that card.

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
Card 6 has no winning numbers, so it is worth no points.
So, in this example, the Elf's pile of scratchcards is worth 13 points.

Take a seat in the large pile of colorful cards. How many points are they worth in total?