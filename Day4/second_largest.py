# def second_largest(array):
#     array.sort()
#     return array[-2]
# array =[3,5,2,4,9]
# a1= second_largest(array)
# print(a1)

def second_largest(array):
    array.sort()
    del array[-1]
    return max(array)
array =[3,5,4,2,4,10,9]
a1= second_largest(array)
print(a1)
