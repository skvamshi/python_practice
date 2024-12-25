from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_elemen_list = []

    for sublist in nested_arr:
        max_in_arr = sublist[0]
        for element in sublist:
            max_in_arr = max(max_in_arr, element)
        max_elemen_list.append(max_in_arr)

    return max_elemen_list


print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))