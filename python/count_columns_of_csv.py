import csv

path = 'C:/Python39/TestFiles/'
filename = 'test.txt'
d = ','
f = open(path + filename,'r')

reader = csv.reader(f,delimiter=d)

# Read first line and count columns
ncol = len(next(reader))

#print out the number of columns
print("There are", ncol, "columns in this file.")

for x in range(1,int(ncol)):
    print(x)

f.seek(0)              # go back to beginning of file
for row in reader:
    print (str(x) + " - " + str(row))
    
