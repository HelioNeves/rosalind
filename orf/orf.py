# Reading lines from files and putting in a content string
# Loading the codon table into a list
contents = []
for line in open('codon_table.txt', 'r').readlines():
        contents.append(line.rsplit())

# Loading the sequence into a input_data string
raw = []
for line in open('rosalind_orf.txt', 'r').readlines():
            raw.append(line.rsplit())

input_data = ''
for h in range(1,len(raw)):
    input_data += raw[h][0]

transcript = input_data.replace('T', 'U').rstrip()


# Transfoming the codon table in a dictionary
codon_table = dict()

for i in range(0,len(contents)):
    for j in range(1,len(contents[0]),2):
        codon_table[contents[i][j-1]]=contents[i][j]


# Checking the position of start codon in input_data
start_codon_pos = []

for k in range(len(transcript)-3):
    if transcript[k:k+3] == 'AUG':
        start_codon_pos.append(k)


# Translating the sequence to protein and verifying if the stop codon
for l in range(len(start_codon_pos)):
    stop_codon = 0
    protein = ''
    while start_codon_pos[l] < len(input_data)-3 and stop_codon == 0:
        if codon_table[transcript[start_codon_pos[l]:start_codon_pos[l]+3]] != 'Stop':
            protein += codon_table[transcript[start_codon_pos[l]:start_codon_pos[l]+3]]
        else:
            stop_codon = 1
        start_codon_pos[l] +=3
    print(str(start_codon_pos[l]) + " :" + protein)

