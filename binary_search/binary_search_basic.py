def binary_search(array, target, start, end):


    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid

        if target > array[mid]:
            start = mid + 1

        else:
            end = mid - 1
    return None


