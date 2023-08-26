import sys


def generate_N_list_with_space():
    """
    # input
    N 입력
    N개의 수를 빈칸을 두고 입력

    # return
    N개의 원소를 가지는 리스트 반환
    """
    N = int(input())
    N_list = list(map(int, sys.stdin.readline().split()))

    return N_list[0:N]


n_list = generate_N_list_with_space()

n = max(n_list) * min(n_list)

print(n)