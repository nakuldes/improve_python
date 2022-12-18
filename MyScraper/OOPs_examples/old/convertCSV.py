import pandas as pd
import sys



read_file = pd.read_excel (sys.argv[1], header=0,dtype='object')



read_file.to_csv (sys.argv[2],
index = None,
header=True,sep = '|',encoding='utf-8') #sep=';' for setting delimiter
df = pd.DataFrame(pd.read_csv(sys.argv[2], delimiter=';', skiprows=0, low_memory=False))

# show the dataframe
df

