def unique(a):
    # checks whether a no in the list is unique with iterative method

    for i in range(len(a)):

        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return False
        return True


def unique2(unsorted):
    # checks whether a no in the list is unique with iterative method
    sort = sorted(unsorted)

    for i in sort:
        if sort[i] == sort[i+1]:
            return False
    return True


