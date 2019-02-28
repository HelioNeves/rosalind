# Reading lines from file and putting in a content string
contents = []
for line in open('rosalind_hamm.txt', 'r').readlines():
        contents.append(str(line.rsplit()))

# A Hamming distance assumes that strings have same lenght
# Then, just iterate them and count the differences
def hamm(word_a, word_b):
    count = 0
    for i in range(0, len(word_a)):
        if word_a[i] != word_b[i]:
            count += 1
    print(count)

hamm(contents[0], contents[1])
