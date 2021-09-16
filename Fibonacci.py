def fib(num1, num2, n):

    for i in range(num1, n+1):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3
        i += 1


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        fib = n + fibonacci(n-1)
        return fib


num1 = 1
num2 = 2
n = 11
fibonacci(n)
print(fibonacci(n))

