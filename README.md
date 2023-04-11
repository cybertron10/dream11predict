# Dream11predict
Generate all possible combination of teams without cap and vc for dream11 fantasy game

The Python Script reads the fixed player names from the first file and generates the remaining player names based on the length of the fixed player list.

The script reads the fixed player names from the first file and calculates the number of remaining players needed to generate a full team of 11 players. It then reads the remaining player names from the second file and generates all possible combinations of num_remaining_players players from the list of remaining players. Finally, it creates all possible team combinations by adding the fixed player names to the randomly selected players and prints them out.

To run this script, you can use the same command as before:

```
python generate_team.py fixed_players.txt remaining_players.txt
```
Just make sure that the first file (fixed_players.txt) contains at least 1 player name, and the second file (remaining_players.txt) contains at least 11 - len(fixed_players) player names, or else the script will not be able to generate any team combinations.
