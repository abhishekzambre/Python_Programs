def convert(num, b1, b2):
    dict = {str(i): i for i in range(0, 10)}
    dict["A"] = 10
    dict["B"] = 11
    dict["C"] = 12
    dict["D"] = 13
    dict["E"] = 14
    dict["G"] = 15

    print(dict)

    total = []

    while num != 0:
        total = (num % 10)




print(convert(123, 7, 13))
