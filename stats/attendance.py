# Let's answer the question: 'How has All-star game attendance changed over time?'

import pandas as pd
import matplotlib.pyplot as plt
from data import games

attendance = games.loc[(games['multi2'] == 'attendance') & (games['type'] == 'info'), ['year', 'multi3']]

attendance.columns = ['year', 'attendance']

#convert to nummeric:
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])