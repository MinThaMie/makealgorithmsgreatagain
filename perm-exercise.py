from perm import *
import copy
import math
# # Create a test permutation of length 20
# q = test_permutation(20)
# print("20: ", q)
# # Define a permutation of length 10
# p=[1,2,3,0,5,4,6,7,8,9]
# print(p)
# print_permutation(p)
# print("is_trivial ", is_trivial(p))
# print(p[0])
# print("cycles: ", cycles(p))
#
# # Create a trivial permutation of length 10
# r = trivial_permutation(10)
# print("trivial ", r)
# Create from cycles
# p1 = permutation_from_cycles(10, [[0, 1, 2, 3], [4, 5]])
# print(p1)
# print_permutation(p1)
# #compare perms
# p=[1,2,3,0,5,4,6,7,8,9]
# p2 = [1,2,4,0,5,3,6,7,8,9]
# print(p1 == p)
# print(p2 == p1)

# it uses index so perms should include zero
def composition(q, p):
    result = []
    for i in p:
        result.append(q[i])
    return result
#
# p=[1,2,3,0,5,6,4,8,7]
# print_permutation(p)
# q = composition(p, p)
# print_permutation(q)
# p1 = [4,3,2,1,0]
# p2 = [1,3,0,2,4]
# q = composition(p1, p2)
# print_permutation(q)

def inverse(p):
    result = copy.deepcopy(p)
    i = 0
    while i < len(p):
        result[p[i]] = i
        i = i + 1
    return result

# p = [1,4,3,2,0]
# q = inverse(p)
# print(q)

def power(perm, pow):
    if pow == 0:
        return trivial_permutation(len(perm))
    elif pow == 1:
        return perm
    elif pow == 2:
        return composition(perm, perm)
    elif pow > 2:
        perm = composition(perm, power(perm, pow - 1))
    elif pow == -1:
        return inverse(perm)
    elif pow < -1:
        perm = inverse(power(perm, pow * -1)) # the relation between -3 and 3 is that the result is its inverse
    return perm

# a=[9,7,4,1,2,0,5,3,6,8]
# print("power: ",power(a,9))
# print("power: ", power(a, -3))
# print_permutation(a)
# print_permutation(power(a, -3))

def period(p):
    i = 1
    while not is_trivial(power(p, i)):
        i = i + 1
    print(i)
    print_permutation(power(p, i))
    return i

# p = permutation_from_cycles(5,[[0,1,2,3,4]])
# print(p)
# print_permutation(p)
# period(p)
# p = test_permutation(6)
# print_permutation(p)
# period(p)
# p = test_permutation(10)
# print_permutation(p)
# period(p)
# print_permutation(power(p, 120))
#

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

#  lcm = a*b / gcd(a,b)
def calc_lcm(a, b):
    return a * b // gcd (a, b)

def period2(p):
    all_cycles = cycles(p)
    if len(all_cycles) == 1:
        return len(all_cycles)
    else:
        periods_cycle = []
        for c in all_cycles:
            periods_cycle.append(len(c))
        lcm = calc_lcm(periods_cycle[0], periods_cycle[1])
        i = 2
        while i < len(periods_cycle):
            lcm = calc_lcm(lcm, periods_cycle[i])
            i = i + 1
        return lcm


p = test_permutation(200)
print_permutation(p)
print("period for 200: ", period2(p))
