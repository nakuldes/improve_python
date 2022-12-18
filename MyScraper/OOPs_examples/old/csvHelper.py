"""
Author : Nakul
email : n.d.3690@gmail.com

This script allows to run PostgreSQL commands of type DCL.

Run requirement_fulfil.py file on firsttime usage to install dependency 
Required input csv file.
Input SQL query.
e.g. select * from csv
Optoin to save query result
"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import sys

class CSVtoSQL:
    """Method to read csv file"""
    def read_csv_file(self,filename):
        self.file = filename
        try:
            #self.file = 'sealevel'
            df = pd.read_csv(self.file+'.csv')
            print(df.head())
            return df
        except FileNotFoundError as err:
            print(f"{err}, {type(err)=}")
            raise
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
        

    def load_csv_to_db(self, query, df_of_csv):
        """Method to RUN sql command"""
        try:
            engine = create_engine('sqlite://', echo = False)
            df_of_csv.to_sql('csv', con=engine, if_exists='replace')
            #query = 'SELECT Year,GMSL_noGIA from csv WHERE year=1994'
            result = engine.execute(query).fetchall()
            print(df_of_csv)
            for row in result:
                print(row)
            return result
        
        except OperationalError as err:
            print(f"{err}, {type(err)=}\n\n")
            retry = input('Do you want to retry? y/n  :')
            if retry == 'y':
                print('Enter sql query')
                sql_q = input()
                #print(sql_q)
                self.load_csv_to_db(sql_q, df_of_csv)
            else:
                print('Closing the script')
                sys.exit() 

        except BaseException as err:
            print(f"{err}, {type(err)=}")
            raise

    def save_to_csv(self, result, out_file_nane):
        """Method to save result"""
        try:
            df2 = pd.DataFrame(data=result)
            df2.to_csv(out_file_nane+'.csv')
            
            print('Result saved in {}.csv'.format(out_file_nane))
        except BaseException as err:
            print(f"{err}, {type(err)=}")
            raise




if __name__ == '__main__':
    print('Starting CSV to SQL App \n\n')
    print('Enter csv file name to read')
    filename = input()
    obj = CSVtoSQL()

    getdf = obj.read_csv_file(filename)
    print('File opened successfully')
    resume = 'y'
    while resume == 'y':
        print('Enter sql query')
        sql_q = input()
        get_result = obj.load_csv_to_db(sql_q,getdf)
        print('\t \t ..end of query result')
        resume = input('For another query > Press "y" OR "n" to get save option \n')

    save_result = input('Press "y" to save current query output \n')
    if save_result == 'y':
        print('Enter output file name or press enter to generate csv immediately ')
        out_filename = input()
        out_filename = 'output' if out_filename == '' else out_filename
        exec_status = obj.save_to_csv(get_result, out_filename)
    else:
        print('Exited without saving result.')

    print('execution completed')

