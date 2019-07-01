#Reading the line from file and putting in a content string
line = open('rosalind_rna.txt', 'r').readline()

'''METHOD 1 Iteration
Iterating across the input string, character by character
and as strings are immutable, we made a new one
'''
input_iteration = str()
for i in range(len(line)):
    if line[i] == 'T':
        input_iteration += 'U'
    else:
        input_iteration += line[i]

'''METHOD 2 Replace
Using the python's inbuilt method replace()
'''
input_replace = line.replace('T', 'U')

#If the two strings are equal, then print
if input_iteration == input_replace:
    print(input_iteration)