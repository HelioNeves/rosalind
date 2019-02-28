# Reading lines from file and putting in a content string
contents = []
for line in open('rosalind_subs.txt', 'r').readlines():
            contents.append(line.rstrip())

s = contents[0]
t = contents[1]
motif_bz = ''
motif_bo = ''

for i in range(0,len(s)-len(t)):
    if s[i:i+len(t)] == t:
        motif_bz += str(i) + ' '
        motif_bo += str(i+1) + ' '

print(motif_bo)

