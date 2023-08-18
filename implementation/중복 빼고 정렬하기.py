import sys


def generate_n_list_with_space():
    """
    # input
    N 입력
    N개의 수를 빈칸을 두고 입력

    # return
    N개의 원소를 가지는 리스트 반환
    """
    n = int(input())
    n_list = list(map(int, sys.stdin.readline().split()))

    return n_list[0:n]


n_list = sorted(list(list(set(generate_n_list_with_space()))))

for i in n_list[0:len(n_list) - 1]:
    print(i, end=" ")
print(n_list[-1])
