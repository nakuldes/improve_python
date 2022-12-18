
import pandas as pd

dataframe_ex2 = pd.read_excel('.\Pandas\ex3.xlsx', sheet_name='Sheet1', header=0, names= [0,3])
dataframe_ex2 = dataframe_ex2.dropna(axis=1, how='any')
print(dataframe_ex2)
rows = len(dataframe_ex2.index)
with open('./Pandas/row_counter.txt', 'r+') as txtfile:
    prev_rows = int(txtfile.read())
    if(prev_rows<rows):
        #txtfile.seek(0)
        #txtfile.write(str(rows))
        #txtfile.truncate()
        print(rows)
        print('********************************')

        for row_index in range(prev_rows, rows):
            last_row_values = dataframe_ex2.iloc[[row_index]]
            #last_dict = last_row_values.to_dict()
            #col1 = last_row_values['Customer Ship-To Name']
            ls = last_row_values
            print(ls)
            for r in last_row_values.items():
                print(r)
        # for each_row in last_dict:
        #     for k, v in last_dict.items():
        #         print(k, v)


