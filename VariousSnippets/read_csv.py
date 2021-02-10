import csv

path = 'C:\Python39\TestFiles\\'

with open(path + '20201204105031_invticket_1189.csv') as csv_file:
    #dialect = csv.Sniffer().sniff(csv_file.read(1024))
    #csv_file.seek(0)
    #reader = csv.reader(csv_file, dialect)

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    #BEGIN FOR
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif {row[0]} == "ooking Number":
            print('nothing here')
            line_count -= 1
        else:
            print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]},')
            line_count += 1

        #INSERT UPDATE FOR EACH FIELD WHERE BOOKING NUMBER = {row[1]}
#       IF {row[0]} IS NOT NULL:
#           UPDATE <table> SET <field> = {row[0]} where bookingnummber = {row[1]}')    
#       IF {row[2]} IS NOT NULL:
#           UPDATE <table> SET <field> = {row[2]} where bookingnummber = {row[1]}    
#       IF {row[3]} IS NOT NULL:
#           UPDATE <table> SET <field> = {row[3]} where bookingnummber = {row[1]}    
#       IF {row[4]} IS NOT NULL:
#           UPDATE <table> SET <field> = {row[4]} where bookingnummber = {row[1]}    
#       IF {row[5]} IS NOT NULL:
#           UPDATE <table> SET <field> = {row[5]} where bookingnummber = {row[1]}    
    #END FOR
            
    print(f'Processed {line_count} lines.')
