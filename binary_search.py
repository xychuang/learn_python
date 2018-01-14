def binary_search(arr,x):
    lo = 0
    hi = len(arr) - 1
    while (lo < hi):
        mid = (lo + hi) // 2
        if arr[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo if arr[lo] == x else -1

"""
arr = [4, 7, 7, 9, 10, 10, 10, 18]; x = 11 -> index(18) = 7f
x = 10 -> index(first 10) = 4
x = 0 -> 0
"""

def bisect_left(arr, x):
    lo = 0
    hi = len(arr)
    while (lo < hi):
        mid = (lo + hi) // 2
        if arr[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
        return lo

print(bisect_left([4, 7, 7, 9, 10, 10, 10, 18],10))
print(bisect_left([4, 7, 7, 9, 10, 10, 10, 18],18))

def bisect_right(arr, x):
    lo = 0
    hi = len(arr)
    while (lo < hi):
        mid = (lo + hi) // 2
        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo

print(bisect_right([4, 7, 7, 9, 10, 10, 10, 18],10))
print(bisect_right([4, 7, 7, 9, 10, 10, 10, 18],0))
print(bisect_right([4, 7, 7, 9, 10, 10, 10, 18],7))
