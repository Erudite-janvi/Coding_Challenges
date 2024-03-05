def selection_sort(array,size):
    for i in range(size):
        min_index = i
        for j in range (i+1,size):
            if array[j] < array[min_index]:
                min_index = j
                array[min_index],array[i]=array[i],array[min_index]
arr = [2,3,7,4,3,1,8]
size = len(arr)
selection_sort(arr,size)
print(arr)                