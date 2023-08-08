array = [7, 5, 8, 1, 3, 2, 4, 9, 0]


def quick_sort_array(start, end, array):
    if start > end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피봇보다 큰 값을 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피봇보다 작은 값 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 서로 교차하는 지점인 경우
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 교차하지 않는 경우
        else:
            array[left], array[right] = array[right], array[left]

    # 피봇을 기준으로 분할하여 같은 동작을 반복
    quick_sort_array(start, right - 1, array)
    quick_sort_array(right + 1, end, array)
    return array


print(quick_sort_array(0, len(array) - 1, array))
