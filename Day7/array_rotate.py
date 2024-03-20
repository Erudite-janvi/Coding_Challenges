def rotate(arr, d):
    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
print(rotate(arr, 2))

