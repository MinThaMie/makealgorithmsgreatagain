class Calculator:
    def multiples(self):
        number = int(input("number "))
        total = 0
        for i in range(0, number):
            if i % 3 == 0 or i % 5 == 0:
                total = total + i
        print(total)


Calculator().multiples()
