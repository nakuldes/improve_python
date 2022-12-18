from operator import index
from typing import List
import pandas as pd
from datatest import validate
import sys

#null_validation = [CustomElementValidation(lambda d: d is not np.nan, 'this field cannot be null')]

lst: List = ['one', 'two' , 'three']

file = ".\Pandas\FORTSMITHPAPER_01012022_01312022.xlsx"
outfile = ".\Pandas\out_FORTSMITHPAPER_01012022_01312022.xlsx"

df = pd.read_excel(file)
df.to_csv(outfile)

for ins, values in df.items():
    print(values)
    val = df[str(values[0])].isnull()
    print(val)
#check_if_all_cols_avl = col_val.__contains__('False')

#print(check_if_all_cols_avl)

row_remove_filter = df.dropna(axis=0, how='all')
row_remove_filter.to_excel(outfile , index=False)
