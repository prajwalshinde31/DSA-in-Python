def find_median_sorted_arrays(nums1, nums2):
    merged = nums1 + nums2
    print(merged)
    ordered = sorted(merged)
    print(ordered)
    n = len(ordered)
    print(n)
    mid = n // 2
    print(mid)

    if n == 0:
        return 0
    elif n % 2 == 0:
        med = (ordered[mid] + ordered[mid - 1]) / 2
        return med
    elif n % 2 != 0:
        return ordered[mid]


a = [15, 11, 21, 9]
b = [52, 14, 41, 6, 2, 9]

print(find_median_sorted_arrays(a, b))
