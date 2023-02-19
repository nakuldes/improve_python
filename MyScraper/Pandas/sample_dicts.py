# This is dict sample for practice

import pandas as pd

df = pd.read_excel('pandas\excle4.xlsx')

df1 = df.dropna()
df.to_csv('it1.csv')
