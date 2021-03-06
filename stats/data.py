import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
#game_files now contains a list of all file names that end with .EVE in the games folder.

# To better prepare the game_files list for reading into pandas, sort it in place by calling sort().

game_files.sort()

# Note: There are two sorting functions in Python. To sort in place use list.sort(), not sorted(list) which returns a new list.

game_frames = []

for game_file in game_files:
    game_frame = pd.read_csv(game_file, names = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])

    game_frames.append(game_frame)

games = pd.concat(game_frames)
#We now have a large DataFrame called games that contains all of the data from all of the event files.

#CLEAN UP DATA:
#Use the loc[] function to select rows that have a value of ?? in the multi5 column in the games DataFrame.
#Replace ?? with an empty string.
games.loc[ games['multi5'] == '??', 'multi5'] = ''

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')#r stands for 'regular expression'

identifiers = identifiers.fillna(method = 'ffill')

#CHANGE COLUMN NAMES
identifiers.columns = ['game_id', 'year']

games = pd.concat([games, identifiers], axis = 1, sort = False)

games = games.fillna(' ')

#To slightly reduce the memory used by the games DataFrame we can provide Pandas with a clue to what data is contained in certain columns.
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

print(games.head())