# Reading lines from file and putting in a content string
for line in open('rosalind_iev.txt', 'r').readlines():
        contents = line.rsplit()

AA_AA = float(contents[0])
AA_Aa = float(contents[1])
AA_aa = float(contents[2])
Aa_Aa = float(contents[3])
Aa_aa = float(contents[4])
aa_aa = float(contents[5])


def iev_prob(offsprings, AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa):
        allel_prob = [1, 1, 1, 0.75, 0.5, 0]
        AA_AA *= allel_prob[0]
        AA_Aa *= allel_prob[1]
        AA_aa *= allel_prob[2]
        Aa_Aa *= allel_prob[3]
        Aa_aa *= allel_prob[4]
        aa_aa *= allel_prob[5]

        return offsprings*(AA_AA+AA_Aa+AA_aa+Aa_Aa+Aa_aa+aa_aa)

print(iev_prob(2, AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa))
