array = [7, 5, 8, 1, 3, 2, 4, 9, 0]


# i번째 작은 데이터를 선택 후 i번째 위치로 이동
def selection_sort_array(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort_array(array))
