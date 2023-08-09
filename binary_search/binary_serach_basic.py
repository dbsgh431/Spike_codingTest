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


print(binary_search([0,1,2,3,4,5,6,7], 3, 0, 8))