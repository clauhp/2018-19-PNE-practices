<<<<<<< Updated upstream
def fibonacci_sr(n):
    a = 0
    b = 1
    num = n
    for i in range(num):
        x = print(a, end=' , ')
        nth = a + b
        a = b
        b = nth
    return x
serie = fibonacci_sr (int(input("Please, inserte the number you want: ")))
print (serie)
=======
n = int(input("Please, introduce a number: "))
serie = 0
for num in range(n):
    serie = num + n[num-1]
    print (serie)
>>>>>>> Stashed changes
