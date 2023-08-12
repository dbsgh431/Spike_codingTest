import sys
from typing import List


def generate_N_list_with_space():
    """
    # input
    N 입력
    N개의 수를 빈칸을 두고 입력

    # return
    N개의 원소를 가지는 리스트 반환
    """
    N = int(input())
    N_list: list[int] = list(map(int, sys.stdin.readline().split()))

    return N_list[0:N]


array = generate_N_list_with_space()

amount = int(input())

start, end = 1 , max(array)

if sum(array) <= amount:
    print(end)
else:
    while start <= end:
        mid = int((start + end) / 2)

        total_budget = 0

        for i in array:
            if i < mid:
                total_budget += i
            else:
                total_budget += mid

        if total_budget == amount:
            end = mid
            break

        if total_budget < amount:
            start = mid + 1

        else:
            end = mid - 1

    print(end)

