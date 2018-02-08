def sum_even_fib():
    a = 0
    b = 1
    sum = 0
    while a < 4000000:
        a , b = b, a+b
        if b % 2 == 0:
            sum = sum + b
    print(sum)

sum_even_fib()