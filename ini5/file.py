#Reading lines from file and putting in a list
contents = []
for line in open('rosalind_ini5.txt', 'r').readlines():
        contents.append(line.strip('\n'))

#Printing the even numbered lines, starting by one
for i in range(1, len(contents), 2): 
    print(contents[i])
