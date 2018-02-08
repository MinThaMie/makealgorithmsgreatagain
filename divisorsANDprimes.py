def all_divisors(a):
    divs = []
    i = 1
    while i <= a:
        if a % i == 0:
            divs.append(i)
        i = i + 1
    # print(divs)
    return divs

all_divisors(12)

def is_a_prime(n):
    return len(all_divisors(n)) == 2

def prime_factorisation(a):
    divs = all_divisors(a)
    prime_factors = []
    if len(divs) == 2:
        print("it's already a prime")
        return divs
    else:
        for i in divs[1:]:
            if is_a_prime(i):
                prime_factors.append(i)
                f = a // i
                if is_a_prime(f):
                    prime_factors.append(f)
                    break
                else:
                    prime_factors.extend(prime_factorisation(f))
                    break
    return prime_factors

prime_factorisation(6)
print(prime_factorisation(13195))
def max_primefact(n):
    res = max(prime_factorisation(n))
    print(res)
    return res

# max_primefact(600851475143)
# als je de wortel neemt en dan naar beneden loopt is het efficienter