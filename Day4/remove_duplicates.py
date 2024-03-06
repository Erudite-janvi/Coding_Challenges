# def remove_duplicate(array):
#     unique_elements = []
#     for element in array:
#         if element not in unique_elements:
#             unique_elements.append(element)
#     return unique_elements
# array = [2,3,7,4,3,1,4,4,8]   
# print(remove_duplicate(array))     
# def remove_duplicate(array):
#     unique_list = list(set(array))
#     return unique_list
# array = [2,3,7,4,3,1,4,4,8]
# print(remove_duplicate(array))
def count_duplicates(array):
    element_count = {}
    
    for element in array:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    return element_count

array = [2, 3, 7, 4, 3, 1, 4, 4, 8]
print(count_duplicates(array))
