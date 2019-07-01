# Reading lines from fasta and putting from a list to a dict
dna = dict()
contents = []
for line in open('rosalind_grph.txt', 'r').readlines():
    contents.append(line.strip('\n'))
    if line[0] == '>':
        header = line[1:].rstrip()
        dna[header] = ''
    else:
        dna[header] = dna.get(header) + line.rstrip()


def graph_dna(fasta_dictionary, k_frame):
        result = ""

        for s in fasta_dictionary:
                for t in fasta_dictionary:
                        if (s != t) and (fasta_dictionary.get(s)[-k_frame:] == fasta_dictionary.get(t)[:k_frame]):
                                result += s + " " + t + "\n"
        return result

print(graph_dna(dna, 3))        
