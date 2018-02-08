def largest_palindrome():
    b = 999
    palindrome = 0

    while b > 0 and b >= palindrome / b:
        a = b
        while a >= palindrome / b:
            mult = a * b
            string = str(mult)
            if string == string[::-1]:
                palindrome = mult
            a = a - 1
        b = b - 1
    print("The final answer is: ", palindrome, " " , a ," * ", b )

largest_palindrome()