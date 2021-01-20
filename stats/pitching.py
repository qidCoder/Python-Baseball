import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games.[games['type'] == 'play']

strike_outs = plays[plays['event'].str.contains('K')]

#group by year and then by id
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
#.size() added a new column with the number of strikeouts in the game

# convert groupy object to a dataframe
strike_outs = strike_outs.reset_index(name='strike_outs')

strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

#plot
strike_outs.plot(x = 'year', y = 'strike_outs', kind= ' scatter').legend(['Strike Outs'])

plt.show()