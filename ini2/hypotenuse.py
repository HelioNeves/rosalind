#Load the content of file as a single line
f = open("rosalind_ini2.txt", "r")
line = str(f.readline()).split()

#Ensure that values are read as numbers for hypotenuse formula
a = int(line[0])
b = int(line[1])
hypo = a**2 + b**2

print(hypo)
