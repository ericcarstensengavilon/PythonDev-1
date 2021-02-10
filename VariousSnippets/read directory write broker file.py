import os
import csv
import pyodbc

location = 'C:/Python39/TestFiles/'
substring = 'BrokerFeeVouch'

#Create new csv file to write to
#https://www.golinuxcloud.com/python-write-to-file/#Syntax_to_open_files_with_the_open()_function
FILE_WRITE = open('C:/Python39/TestFiles/test.txt','a')

#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    if file.endswith(".csv"):
        if substring in file:
        
        #if substring=" * "+substring+" * "

        #Open the file
            with open(os.path.join(location, file)) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    
                    #BEGIN FOR
                    for row in csv_reader:
                        if line_count == 0:
                            #print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:
                            #Print to screen
                            print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}')

                            #Write to a text file
                            FILE_WRITE.write(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}\n')

                            line_count += 1

FILE_WRITE.close()

                
                #print((file))
                #print()
                #print(os.path.join(location, file))



