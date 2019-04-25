num = int(input("Please, inserte the number you want: "))
a, b = 0, 1

for i in range(num):
    print(a, end=' ')
    nth = a + b
    a = b
    b = nth
