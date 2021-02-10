import os
import csv

location = 'C:/Python39/DEVFiles/PythonDev/AgEcon/'


#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    if file.endswith(".json"):

        #Open the file
        with open(os.path.join(location, file)) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0

                print(file)
                
                        


