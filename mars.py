import string

def encode(number):
    alphabet = string.ascii_uppercase
    if number <= 8:
        print(number)
        return number
    else:
        print(alphabet[number - 9])
        return alphabet[number - 9]
#
# encode(7)
# encode(9)
# encode(10)

# Only valid with bases < 36
def to_k(n, k):
    digs = string.digits + string.ascii_uppercase
    rest = n
    solution = ""
    while rest != 0:
        (rest, result) = divmod(rest, k)
        solution = solution + digs[result]
    solution = solution[::-1]
    print(solution)
    return solution

to_k(100, 10)
to_k(4321, 16)

def decode(code):
    if code.isalpha():
        result = string.ascii_uppercase.index(code) + 10
        return result
    else:
        return int(code)

# decode("A")
# decode("0")
# decode("Z")

def from_k(s, k):
    inp = s[::-1]
    i = 0
    total = 0
    for c in inp:
        total = total + (decode(c) * (k ** i))
        i = i + 1
    print(total)
    return total

from_k("10E1", 16)
from_k("100", 10)

def convert(k, m, s):
    innumbers = from_k(s, k)
    translated_num = to_k(innumbers, m)
    print(translated_num)

#k = 2, m = 4 and s = 10011010 outputs 2122
convert(2, 4, "10011010")
#k = 16, m = 7 and s = B48C03 is 202400366
convert(16, 7, "B48C03")