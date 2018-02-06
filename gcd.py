def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    print("gcd: ", a)
    return a


# gcd(3141, 156)


def largest_sqaure(length, width):
    tile_size = gcd(length, width)
    area = tile_size * tile_size
    print("area: ", area)


#largest_sqaure(12345678, 987654321)


def frac(a, b):
    while gcd(a, b) != 1:
        greatest = gcd(a, b)
        a, b = a/greatest, b/greatest
    print(a, b)

frac(-24, 60)