# Reading lines from files and putting in a content string
# Loading the codon table into a list
contents = []
for line in open('codon_table.txt', 'r').readlines():
        contents.append(line.rsplit())

# Loading the sequence into a input_data string
for line in open('rosalind_prot.txt', 'r').readlines():
            input_data = line.rsplit()

# Transfoming the codon table in a dictionary
codon_table = dict()

for i in range(0,len(contents)):
    for j in range(1,len(contents[0]),2):
        codon_table[contents[i][j-1]]=contents[i][j]


# Checking the position of start codon in input_data
start_codon_pos = 0
translate = 0

while start_codon_pos < len(input_data[0]) and translate == 0:
    if input_data[0][start_codon_pos:start_codon_pos+3] == 'AUG':
        translate = 1
    else:
        start_codon_pos += 1

# Translating the sequence to protein and verifying if the stop codon
stop_codon = 0
protein = ''

while start_codon_pos < len(input_data[0]) and stop_codon == 0:
    if codon_table[input_data[0][start_codon_pos:start_codon_pos+3]] != 'Stop':
        protein += codon_table[input_data[0][start_codon_pos:start_codon_pos+3]]
    else:
        stop_codon = 1
    start_codon_pos +=3

print(protein)


