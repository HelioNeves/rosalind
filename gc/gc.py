# Reading lines from file and putting from a list to a dict
dna = dict()
contents = []
for line in open('rosalind_gc.txt', 'r').readlines():
    contents.append(line.strip('\n'))
    if line[0] == '>':
        header = line[1:].rstrip()
        dna[header] = ''
    else:
        dna[header] = dna.get(header) + line.rstrip()

# Using the rstrip method above to remove text format fragments (like \n or \t)
# and the list greather will receive our final result
greather = ['', 0, '']

for key in dna:
    gc_qtd = 0
    for i in range(len(dna.get(key))):
        if dna.get(key)[i] == 'G' or dna.get(key)[i] == 'C':
            gc_qtd += 1
    gc_percent = 100*gc_qtd/(len(dna.get(key)))
    if gc_percent > greather[1]:
        greather[0] = key
        greather[1] = gc_percent
        greather[2] = dna.get(key)


print(greather[0], '\n', greather[1])

