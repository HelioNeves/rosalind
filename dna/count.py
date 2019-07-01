#Reading the line from file and putting in a content string
line = open('rosalind_dna.txt', 'r').readline()

#A list to store the nucleotide count in the order ACGT
result = [0, 0, 0, 0]

#Iterating accross the input string, character by character
for i in range(len(line)):
    if   line[i] == 'A':
        result[0] += 1
    elif line[i] == 'C':
        result[1] += 1
    elif line[i] == 'G':
        result[2] += 1
    elif line[i] == 'T':
        result[3] += 1
        
#1st: using map to convert each int value to string
#2nd: separating the result by spaces, then printing
res = " ".join(map(str,result))
print(res)
