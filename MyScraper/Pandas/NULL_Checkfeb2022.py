import pandas as pd
import sys

out=''

#file = sys.argv[1]
file = ".\Pandas\ex2.xlsx"
file_out = ".\Pandas\out_ex2.csv"

fileType = file[len(file)-3:len(file)]

#print fileType

if(fileType != "csv"):
    d={}
    read_file = pd.read_excel (file ,header=0,dtype='object')
    dfs = pd.DataFrame(d)
    dfs

    read_file.to_csv (file_out,  
                      index = None,
                      header=True,sep = ';',encoding='utf-8')  #sep=';' for setting delimiter
    df = pd.DataFrame(pd.read_csv(file_out, delimiter=';', skiprows=0, low_memory=False))
    
    # show the dataframe
    print(df)
    #| df['Distributor Location Name'].isnull() | df['Distributor Sales Rep Number'].isnull() | df['Distributor Sales Rep Name'].isnull() | df['Diversey Rebate Contract Number'].isnull() | df['Ship-To Address2'].isnull() | df['Bill-To Address2'].isnull()
    #Diversey rebate contract is less than 1 or not
    mask1 = df['Diversey Rebate Contract Number'].isnull()
    mask2 = df['Diversey Rebate Contract Number'].apply(lambda x: True if x < 1 else False)
    
    if mask1.any()== 1 or mask2.any() == 0:

        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['UOM'].isnull()
    else:    
        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Bill-To Address'].isnull() | df['Bill-To City'].isnull() | df['Bill-To State'].isnull() | df['Bill-To Zip'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Ship-To Address'].isnull()| df['Ship-To City'].isnull()| df['Ship-To State'].isnull()| df['Ship-To Zip'].isnull()| df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['Rebate Amount Requested'].isnull()| df['UOM'].isnull()

else:
    df = pd.DataFrame(pd.read_csv(sys.argv[1], delimiter=',', skiprows=0, low_memory=False))
     
    # show the dataframe 
    df
    #Diversey rebate contract is less than 1 or not
    mask1 = df['Diversey Rebate Contract Number'].isnull()
    mask2 = df['Diversey Rebate Contract Number'].apply(lambda x: True if x < 1 else False)
    #| df['Distributor Location Name'].isnull() | df['Distributor Sales Rep Number'].isnull() | df['Distributor Sales Rep Name'].isnull() | df['Diversey Rebate Contract Number'].isnull() | df['Ship-To Address2'].isnull() | df['Bill-To Address2'].isnull()
    if mask1.any()== 1 or mask2.any() == 0:
        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['UOM'].isnull()
    else:    
        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Bill-To Address'].isnull() | df['Bill-To City'].isnull() | df['Bill-To State'].isnull() | df['Bill-To Zip'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Ship-To Address'].isnull()| df['Ship-To City'].isnull()| df['Ship-To State'].isnull()| df['Ship-To Zip'].isnull()| df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['Rebate Amount Requested'].isnull()| df['UOM'].isnull()
    
#print mask
if mask.any() == 1 :
    out='Reject'
 
print(out)