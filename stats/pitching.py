import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games.loc[games['type'] == 'play', :]