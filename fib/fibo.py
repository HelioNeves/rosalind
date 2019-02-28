# Reading lines from file and putting in a content string
for line in open('rosalind_fib.txt', 'r').readlines():
        contents = line.split()

# n as generations
# k as offsprings
n = int(contents[0])
k = int(contents[1])

# A Fibonacci function with k descendants each round
def fibo(gen, pairs):
    if gen > 2:
        return fibo(gen-1, pairs) + fibo(gen-2, pairs)*pairs
    else:
        return 1

print(fibo(n,k))
