def fact(n):
    k = 1
    t = 1
    while k < n:
        k = k + 1
        t = t * k
    print("factorial: ", t)
    return t

fact(28)

def binom(n, k):
    print("binomial: ", fact(n) // (fact(n-k) * fact(k)))

binom(12,8)
binom(40,2)
