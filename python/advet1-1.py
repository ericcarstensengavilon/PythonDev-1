import csv

path = 'C:\AdventOfCode\\'

with open(path + 'AdventDay1Puzzle1.txt') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    adj = ["red", "big", "tasty"]

    #BEGIN FOR
    # Loop through each number
    for rowa in csv_reader:
        
        # Sub loop through each number starting with the next number in line.
        for rowb in adj:
            num1 = f'\t{rowa[0]}'
            num2 = f'\t{rowb[0]}'
            print(num1)
            print(num2)
       
