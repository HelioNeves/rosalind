# Reading lines from file and putting in a content string
for line in open('rosalind_fibd.txt', 'r').readlines():
        contents = line.split()

# n as generations
# m as months
n = int(contents[0])
m = int(contents[1])

# A Fibonacci function with m-months lifetime in a array
# made by the formula: Fn = Fn-1 + Fn-2 + Fn-(months-1)
def fibd(gen, mon):
    f = [0] * (gen+1)
    f[0] = 1
    for i in range(2, gen + 1):
        f[i] = (f[i-2] + f[i-1] - f[i-mon-1])
    print(f[gen]+f[gen-1])

fibd(n,m)
