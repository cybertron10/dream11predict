import sys
import itertools

# Reading the filename arguments
fixed_filename = sys.argv[1]
remaining_filename = sys.argv[2]

# Opening the fixed player file and reading the player names
with open(fixed_filename, 'r') as f:
    fixed_players = [line.strip() for line in f.readlines()]

# Calculating the number of remaining players needed to generate a full team of 11 players
num_remaining_players = 11 - len(fixed_players)

# Opening the remaining player file and reading the player names
with open(remaining_filename, 'r') as f:
    remaining_players = [line.strip() for line in f.readlines()]

# Generating all possible combinations of num_remaining_players players from the list of remaining players
combinations = list(itertools.combinations(remaining_players, num_remaining_players))

# Creating all possible team combinations by adding the fixed players to the randomly selected players
team_combinations = []
for combo in combinations:
    team_combinations.append(fixed_players + list(combo))

# Printing all possible team combinations
for team in team_combinations:
    print(team)
