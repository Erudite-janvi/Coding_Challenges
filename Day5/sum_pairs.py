def getPairsCount(arr, n, k):
    count = 0
    n = len(arr)
    for i in range (n):
        for j in range (i + 1, n):
         if arr[i] + arr[j] == k:
            count += 1
    return count

arr = [2, 3, 7, 4, 3, 1, 4, 4, 8]
n = len(arr)
k = 4
print(getPairsCount(arr,n,k))