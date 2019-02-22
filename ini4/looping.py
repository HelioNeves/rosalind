#Trying the python csv package: reading lines from file
import csv

with open('rosalind_ini4.txt', newline='') as inputfile:
    results = list(csv.reader(inputfile))

#Filtering the csv fragments
piece_tag = str(results[0])[2:-2].split()

a = int(piece_tag[0])
b = int(piece_tag[1])

#Ensures "a" is odd
if (a%2 == 0):
    a += 1

sum_odd = 0

#Sum from a till b+1 (including b)
for i in range(a, b+1, 2):
    sum_odd = sum_odd + i 
    
print(sum_odd)
