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