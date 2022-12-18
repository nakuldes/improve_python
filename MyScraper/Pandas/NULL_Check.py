import pandas as pd
import sys

out=""

file = ".\Pandas\FORTSMITHPAPER_01012022_01312022.xlsx"
file1 = ".\Pandas\FORTSMITHPAPER_01012022_01312022.xlsx"
file2 =".\Pandas\out_FORTSMITHPAPER_01012022_01312022.csv"
#file = sys.argv[0]

fileType = file[len(file)-3:len(file)]

#print fileType

if(fileType != "csv"):
    

    read_file = pd.read_excel(file,header=0 ,dtype='object')
    row_remove_filter = read_file.dropna(axis=0, how='all')
    row_remove_filter.to_excel(file1, index=False)

    read_file.to_csv (file2,  
                      index = None,
                      header=True,sep = ';',encoding='utf-8')  #sep=';' for setting delimiter
    df = pd.DataFrame(pd.read_csv(file2, delimiter=';', skiprows=0, low_memory=False))
     
    # show the dataframe
    df
    #| df['Distributor Location Name'].isnull() | df['Distributor Sales Rep Number'].isnull() | df['Distributor Sales Rep Name'].isnull() | df['Diversey Rebate Contract Number'].isnull() | df['Ship-To Address2'].isnull() | df['Bill-To Address2'].isnull()
    #Diversey rebate contract is less than 1 or not
    mask3 = df['Distributor Location Code'].isnull() | \
            df['Distributor Location Name'].isnull() | df['Distributor Sales Rep Number'].isnull() | \
            df['Distributor Sales Rep Name'].isnull() | df['Diversey Rebate Contract Number'].isnull()| \
            df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | \
            df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | \
            df['Bill-To Address'].isnull() | df['Bill-To Address2'].isnull() | df['Bill-To City'].isnull() | \
            df['Bill-To State'].isnull() | df['Bill-To Zip'].isnull() | df['Customer Ship-To Account Number'].isnull() | \
            df['Customer Ship-To Name'].isnull() | df['Ship-To Address'].isnull() | df['Ship-To Address2'].isnull() | \
            df['Ship-To City'].isnull() | df['Ship-To State'].isnull() | df['Ship-To Zip'].isnull() | \
            df['Diversey Product Code'].isnull() | df['Diversey Product Description'].isnull() | \
            df['Quantity'].isnull() | df['Rebate Amount Requested'].isnull() | df['UOM'].isnull() | \
            df['Distributor Extended Cost'].isnull() | df['Dist SKU code'].isnull() | df['User Field 1 Code'].isnull() | \
            df['User Field 1 Description'].isnull() | df['User Field 2 Code'].isnull() | df['User Field 2 Description'].isnull() | \
            df['SIC'].isnull() | df['HIN'].isnull()
    mask1 = df['Diversey Rebate Contract Number'].isnull()
    mask2 = df['Diversey Rebate Contract Number'].apply(lambda x: True if x < 1 else False)
    
    
    df = df.dropna(how = 'all')
    if mask1.any()== 1 or mask2.any() == 0:

        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['UOM'].isnull()
    else:    
        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Bill-To Address'].isnull() | df['Bill-To City'].isnull() | df['Bill-To State'].isnull() | df['Bill-To Zip'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Ship-To Address'].isnull()| df['Ship-To City'].isnull()| df['Ship-To State'].isnull()| df['Ship-To Zip'].isnull()| df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['Rebate Amount Requested'].isnull()| df['UOM'].isnull()

else:
    df = pd.DataFrame(pd.read_csv(file, delimiter=',', skiprows=0, low_memory=False))
     
    # show the dataframe 
    print(df)
    mask3 = df['Distributor Location Code'].isnull() | \
            df['Distributor Location Name'].isnull() | df['Distributor Sales Rep Number'].isnull() | \
            df['Distributor Sales Rep Name'].isnull() | df['Diversey Rebate Contract Number'].isnull()| \
            df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | \
            df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | \
            df['Bill-To Address'].isnull() | df['Bill-To Address2'].isnull() | df['Bill-To City'].isnull() | \
            df['Bill-To State'].isnull() | df['Bill-To Zip'].isnull() | df['Customer Ship-To Account Number'].isnull() | \
            df['Customer Ship-To Name'].isnull() | df['Ship-To Address'].isnull() | df['Ship-To Address2'].isnull() | \
            df['Ship-To City'].isnull() | df['Ship-To State'].isnull() | df['Ship-To Zip'].isnull() | \
            df['Diversey Product Code'].isnull() | df['Diversey Product Description'].isnull() | \
            df['Quantity'].isnull() | df['Rebate Amount Requested'].isnull() | df['UOM'].isnull() | \
            df['Distributor Extended Cost'].isnull() | df['Dist SKU code'].isnull() | df['User Field 1 Code'].isnull() | \
            df['User Field 1 Description'].isnull() | df['User Field 2 Code'].isnull() | df['User Field 2 Description'].isnull() | \
            df['SIC'].isnull() | df['HIN'].isnull()
            
        
    #Diversey rebate contract is less than 1 or not
    mask1 = df['Diversey Rebate Contract Number'].isnull()
    mask2 = df['Diversey Rebate Contract Number'].apply(lambda x: True if x < 1 else False)
        
    # if mask3.any() == 0:
    #     df1 = df.dropna(axis=0, how='all')
    # else:
    #     True
    
    #| df['Distributor Location Name'].isnull() | df['Distributor Sales Rep Number'].isnull() | df['Distributor Sales Rep Name'].isnull() | df['Diversey Rebate Contract Number'].isnull() | df['Ship-To Address2'].isnull() | df['Bill-To Address2'].isnull()
    if mask1.any()== 1 or mask2.any() == 0:
        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['UOM'].isnull()
    else:    
        mask = df['Distributor Location Code'].isnull() | df['Distributor Invoice Number'].isnull() | df['Date Shipped'].isnull() | df['Customer Bill-To Account Number'].isnull() | df['Customer Bill-To Name'].isnull() | df['Bill-To Address'].isnull() | df['Bill-To City'].isnull() | df['Bill-To State'].isnull() | df['Bill-To Zip'].isnull() | df['Customer Ship-To Account Number'].isnull() | df['Customer Ship-To Name'].isnull() | df['Ship-To Address'].isnull()| df['Ship-To City'].isnull()| df['Ship-To State'].isnull()| df['Ship-To Zip'].isnull()| df['Diversey Product Code'].isnull()| df['Diversey Product Description'].isnull()| df['Quantity'].isnull()| df['Rebate Amount Requested'].isnull()| df['UOM'].isnull()
    
#print mask
if mask.any() == 1 :
    out = 'Reject'
     
	#df = pd.DataFrame(mask)

# using dropna() function    

print(out)