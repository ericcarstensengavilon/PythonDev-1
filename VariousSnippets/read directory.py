import os
import csv

location = 'C:/Python39/TestFiles/'

#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    if file.endswith(".csv"):

        #Open the file
        with open(os.path.join(location, file)) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0

                #BEGIN READER
                for row in csv_reader:
                    if line_count == 0:
                        #print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    elif {row[0]} == """Booking Number""":
                        #print('nothing here')
                        line_count -= 1
                    else:
                        print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]},')
                        line_count += 1
                #END READER
                        
#print((file))
#print()
#print(os.path.join(location, file))



