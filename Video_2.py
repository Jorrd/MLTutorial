# https://www.youtube.com/watch?v=JcI5Vnw0b2c&index=2&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v
# Sentdex: Regression Intro - Practical Machine Learning Tutorial with Python p2

import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())