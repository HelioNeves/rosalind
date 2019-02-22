#Trying the python csv package: reading lines from file
import csv

with open('rosalind_ini3.txt', newline='') as inputfile:
    results = list(csv.reader(inputfile))

#Filtering the csv fragments
piece = str(results[0])[2:-2]
piece_tag = str(results[1])[2:-2].split()

#Ensures that contents are read as numbers
a = int(piece_tag[0])
b = int(piece_tag[1])
c = int(piece_tag[2])
d = int(piece_tag[3])

#Showing the slices
print(piece[a:b+1], piece[c:d+1])
