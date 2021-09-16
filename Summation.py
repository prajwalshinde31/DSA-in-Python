def summation(arr, n):
    # provides sum of n elements of an array

    if n < 0:
        return 0
    elif n == 0:
        return arr[0]
    else:
        return arr[n] + summation(arr, n-1)



