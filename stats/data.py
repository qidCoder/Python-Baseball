import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
#game_files now contains a list of all file names that end with .EVE in the games folder.

# To better prepare the game_files list for reading into pandas, sort it in place by calling sort().

game_files.sort()

# Note: There are two sorting functions in Python. To sort in place use list.sort(), not sorted(list) which returns a new list.

for game_file in game_files:
    game_frame = pd.read_csv(game_file, names = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
