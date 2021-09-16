def factorial(n):

    if n < 0:
        return -1
    elif n == 0 and n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact = fact * n
            n = n-1
        return fact


facto = factorial(5)
print(facto)
