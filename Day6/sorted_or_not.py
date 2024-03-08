# def sorted_or_not(array):
#     n = len(array)
#     if n==0 or n ==1:
#         return True
#     return array[0] <= array[1] and sorted_or_not(array[1::])
# array = [1,2,3 ,4,5,6,7]
# if sorted_or_not(array):
#     print("Sorted")
# else:
#     print("Not Sorted")    

def ascending(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return "not sorted"
    return "sorted"

array = [1, 2, 3, 4, 5, 6, 7,9,3,4]
print(ascending(array))
