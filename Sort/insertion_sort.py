array = [7, 5, 8, 1, 3, 2, 4, 9, 0]


def insertion_sort_array(array):
    for i in range(1, len(array)):
        for j in range(i, 0, - 1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array


print(insertion_sort_array(array))
