import os
import csv

location = 'C:/Python39/TestFiles/'


#Create new csv file to write to
#https://www.golinuxcloud.com/python-write-to-file/#Syntax_to_open_files_with_the_open()_function
FILE_WRITE = open('C:/Python39/TestFiles/test.txt','a')
                    
#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    if file.endswith(".csv"):
        
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
                            print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}')
                            FILE_WRITE.write(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}\n')
                            line_count += 1


FILE_WRITE.close()

                
#print((file))
#print()
#print(os.path.join(location, file))



