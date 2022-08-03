from pathlib import Path
import csv
import pandas as pd
import numpy as np
import os.path
from os import path

outputReport = 'Report.txt'

rows = []
fields = []
try:
    prompt = input("\nHello Welcome to Fruit basket Application,"
                "\n \nPlease type the path to your file and press 'Enter': ")

    #Testcase validation
    if not prompt.endswith(".csv"):         #testcase1.text to verify this csv. extension file
        print("Not an csv file")
        raise NameError("Not a valid csv file ,please enter csv extension file")
    
    if not path.exists(prompt): #validation to check if csv file doesnot exist in given path
        raise FileNotFoundError("No such file or Directory found. please check the if file exist in given path") 

    with open(outputReport, 'w') as filetowrite:
        with open(prompt, 'r') as filetoread:
            reader = csv.reader(filetoread)
            df = pd.read_csv(filetoread)
            print(df)
            #empty csv file validation -->validate with blank.csv
            if df.empty == True:
                print("your file is empty, please enter header and row data in file")
                raise ValueError("File is empty, please enter header and row data in file ")

            #Header validation against csv file --> validate with headervalidation.csv
            Header_Validation = ['fruit-type', 'age-in-days', 'characteristic1', 'characteristic2']
            if((df.columns.values.tolist() != Header_Validation)):
                raise NameError("Invalid headers", "Please check all header format should match the valid header",Header_Validation)
            #print("testdata.csv is present")
            print(filetoread.name)
            
            
            filetoread.seek(0)
            
            fields = next(reader)
            print("column",fields)
            for row in reader:
                rows.append(row[:2])
            print("data",rows)

            #Count of fruit -> validate with testdata.csv
            print("Total number of fruits:",len(rows))
            filetowrite.write("Total number of fruits \n" + str(len(rows)) + '\n'+'\n')
            

            #Oldest fruit and age -> validate with testdata.csv
            unique_list = []
            count = 0
            for row in rows:
                if row not in unique_list:
                    count += 1
                unique_list.append(row[0])
                    
            unique_list1 = np.unique(unique_list)
            #print("Output list : ", unique_list1)
            print("Total count of distinct fruit types in the basket:",len(unique_list1))
            filetowrite.write("Total count of distinct fruit types in the basket: \n" + str(len(unique_list1)) + '\n'+ '\n')
            
            
            #Oldest fruit and age -> validate with testdata.csv
            HighestNum = df[['age-in-days']].max(numeric_only=True)
            oldestNum = df.loc[df['age-in-days'] == int(HighestNum)]
            oldestNum = oldestNum.drop('characteristic1', axis=1).drop('characteristic2', axis=1)
            print('Oldest fruit & age:\n ' +oldestNum.to_string(index=False) +'\n \n')
            filetowrite.write('Oldest fruit & age:\n ' + oldestNum.to_string(index=False) + '\n'+ '\n')
					
					
            #The number of each type of fruit in decending order (fruit then count)--> validate with testdata.csv
            countType = df.groupby(['fruit-type'])['fruit-type'].count().reset_index(name='count').sort_values(['count'], ascending=False)
            print('The number of each type of fruit in descending order: \n'+ countType.to_string(index=False)  +'\n' + '\n')
            filetowrite.write('The number of each type of fruit in descending order: \n' + countType.to_string(index=False) +'\n'+'\n')
            

            #The various charactersticts (count,color,shape,etc.) of each fruit by type --> validate with testdata.csv
            typeChar = df.groupby(['fruit-type', 'characteristic1', 'characteristic2'])['fruit-type'].count().reset_index(name='count').sort_values(['count'], ascending=False)
            print('The various characteristics (count, color, shape, etc.) of each fruit by type:' + typeChar.to_string(index=False) + '\n' +'\n')
            filetowrite.write('The various characteristics (count, color, shape, etc.) of each fruit by type:\n ' + typeChar.to_string(index=False) + '\n'+ '\n')
            

            #Null or NAN or Empty values in row, Validate with testdatanull.csv 
            if df.isnull().values.any():
                    raise TypeError("File contains null value in row")

            #validation against first column value to random integer values --> validate with testcasecolumn1.csv
            result_column1 =  df['fruit-type'].str.contains('^[a-zA-Z]',regex=True)
            print(result_column1,"fruit-type")

            for index in range(len(result_column1)):

                if result_column1[index] == False:
                    raise ValueError("Numeric value detected in the column1 row.Expected only characters. Please enter only characters..")
        
            #validation against second column value to random character values --> validate with testcasecolumn2.csv
            result_column2 =  df['age-in-days'].astype(str).str.contains('^[0-9.-]',regex=True)
            print(result_column2,"ageindays")

            for index in range(len(result_column2)):

                if result_column2[index] == False:
                    raise TypeError("Character value detected in the column2 row.Expected only numbers. Please enter only numbers..")

            #validation against third column value to random integer values --> validate with testcasecolumn3.csv
            result_column3 =  df['characteristic1'].str.contains('^[a-zA-Z]',regex=True)
            print(result_column3,"characteristic1")

            for index in range(len(result_column3)):

                if result_column3[index] == False:
                    raise ValueError("Numeric value detected in the column3 row.Expected only numbers. Please enter only characters..")
        
            #validation against Fourth column value to random integer values --> validate with testcasecolumn4.csv
            result_column4 =  df['characteristic2'].str.contains('^[a-zA-Z]',regex=True)
            print(result_column4,"characteristic2")
            count = []
            for index in range(len(result_column4)):

                if result_column4[index] == False:
                    raise ValueError("Numeric value detected in the column4 row.Expected only numbers. Please enter only characters..")
            
       
except FileNotFoundError as ex: #validation to check if csv file doesnot exist in given path
        raise FileNotFoundError(ex)
        print("File not created at path, please create file",ex)
