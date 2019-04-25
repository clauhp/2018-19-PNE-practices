def fibonacci(n):
    num1 = 0
    num2 = 1
    count = 0
    for x in range(n+1):
        count += num1
        num1, num2 = num2, (num1+num2)
    return count


parameter = int(input("Please, introduce a number as parameter: "))
fb_serie = fibonacci(parameter)
print("The sum of the first", parameter, "numbers of the Fibonacci series is:", fb_serie)
