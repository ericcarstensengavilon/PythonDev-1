import csv

path = 'C:\Python39\TestFiles\\'
#filename = '20201204105031_invticket_1189.csv'
filename = 'GAVPOS.csv'
d = ','
f = open(path + filename,'r')

reader = csv.reader(f,delimiter=d)

# Read first line and count columns
ncol = len(next(reader))

#print out the number of columns
print("There are", ncol, "columns in this file.")

# go back to beginning of file
f.seek(0)              

#set linecount to 0
line_count = 0

for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif {row[0]} == "ooking Number":
            print('nothing here')
            line_count -= 1
        else:
            #set the number of arguments to the number of columns.
            #argument number array (0,1,2,etc)
            for i in list(range(1, ncol+1 )):
                c = (i-1)  
                a = (f'\t{row[c]},').strip()
                a = a.replace(',','')
                print ("col_" + str(c) + " = '" + str(a) + "'")
                nol = 'col_' + str(c)
                print("nol = " + nol)
line_count += 1


