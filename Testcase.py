#Expected values to receive in CSV file


import pandas as pd
import os.path
from os import path


try:
    prompt = input("\nHello welcome to Fruit basket,"
            "\n \nPlease type in the path to your file and press 'Enter': ")

    #Testcase validation  #testcase1.text to verify this csv. extension file
    if not prompt.endswith(".csv"):
                print("its not an csv file")
                raise NameError("not a valid csv extension,please enter csv file")
    
    if not path.exists(prompt): #validation to check if csv file doesnot exist in given path
        raise FileNotFoundError("No such file or Directory found. please check the if file exist in given path") 


    with open(prompt, 'r') as file:
        df = pd.read_csv(file) #===> Include the headers
        print(df)
        if df.empty == True: #empty csv file validation -->validate with blank.csv
            print("your file is empty, please enter header and row data in file")
            raise ValueError("no data available")
      
        print("testdata.csv is present")

        #Null or NAN or Empty values in row, Validate with testdatanull.csv 
        if df.isnull().values.any():
            raise TypeError("File contains null value in row")
      
         #Header validation against csv file --> validate with headervalidation.csv      
        Header_Validation = ['fruit-type', 'age-in-days', 'characteristic1', 'characteristic2']
    
        if((df.columns.values.tolist() != Header_Validation)):
                raise NameError("invalid headers", "Please check all headers match the valid header",Header_Validation)
    
         #validation against first column value to random integer values --> validate with testcasecolumn1.csv
        result_column1 =  df['fruit-type'].str.contains('^[a-zA-Z]',regex=True)
        print(result_column1,"fruit-type")

        for index in range(len(result_column1)):

            if result_column1[index] == False:
                raise ValueError("Numeric value detected in the column1 row.Expected only characters. Please enter only characters..")
        
         #validation against second column value to random character values --> validate with testcasecolumn2.csv
        result_column2 =  df['age-in-days'].astype(str).str.contains('^[0-9]',regex=True)
        print(result_column2,"ageindays")

        for index in range(len(result_column2)):

            if result_column2[index] == False:
                raise ValueError("Character value detected in the column2 row.Expected only numbers. Please enter only numbers..")

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
                raise ValueError("Numeric value detected in the column4 row.Expected only numbers. Please enter only characters at row number:" )
            
except FileNotFoundError as ex: #validation to check if csv file doesnot exist in given path
        raise FileNotFoundError(ex)
        print("File not created at path, please create file",ex)
   
     