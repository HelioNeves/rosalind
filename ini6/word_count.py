#Loading one line from file and starting a dictionary
for line in open('rosalind_ini6.txt', 'r').readlines():
        contents = line.split()

dictionary = dict()

#Checking if a word from line is in dictionary, then sum the occurrences
for i in range(0, len(contents), 1): 
    if (contents[i] not in dictionary):
        dictionary[contents[i]] = 1
    else:
        dictionary[contents[i]] += 1

#Printing all the words with respective occurrences amount
for key, value in dictionary.items():
    print(key, value)
