# Reading lines from file and putting in a content string
for line in open('rosalind_iprb.txt', 'r').readlines():
        contents = line.rsplit()

dom = float(contents[0])
het = float(contents[1])
rec = float(contents[2])

def dom_prob(k, m, n):
    total = k + m + n
# K = Dominant allele
    k_first = k / total
    kk = k_first * (k-1)/(total-1)
    km = k_first * m/(total-1)
    kn = k_first * n/(total-1)
# M = Hetero allele
    m_first = m / total
    mk = m_first * k/(total-1)
    mm = m_first * (m-1)/(total-1) * 0.75
    mn = m_first * n/(total-1) * 0.5
# N = Recessive allele                                                    
    n_first = n / total
    nk = n_first * k/(total-1)
    nm = n_first * m/(total-1) * 0.5
    nn = n_first * (n-1)/(total-1) * 0
    return kk + km + kn + mk + mm + mn + nk + nm + nn

print(dom_prob(dom, het, rec))
