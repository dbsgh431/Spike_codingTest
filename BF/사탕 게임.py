import sys


def generate_N_list():
    """
    # input
    N 입력
    공백없이 N개의 수 입력

    # return
    N*N개의 원소를 가지는 리스트 반환
    """
    N = int(input())
    n_list = []
    for i in range(N):
        n_list.append(list(sys.stdin.readline().rstrip()))

    return n_list


n_list = generate_N_list()


def horizontal_swap(i, j):
    n_list[i][j], n_list[i][j + 1] = n_list[i][j + 1], n_list[i][j]
    result = check_count(n_list)
    n_list[i][j], n_list[i][j + 1] = n_list[i][j + 1], n_list[i][j]
    return result


def check_count(n_list):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1, n):
            if n_list[i][j] == n_list[i][j - 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

        count = 1
        for j in range(1, n):
            if n_list[j][i] == n_list[j-1][i]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count


def vertical_swap(i, j):
    n_list[i][j], n_list[i + 1][j] = n_list[i + 1][j], n_list[i][j]
    result = check_count(n_list)
    n_list[i][j], n_list[i + 1][j] = n_list[i + 1][j], n_list[i][j]
    return result


max_count_result = 0
n = len(n_list)

for i in range(n):
    for j in range(n):
        if i + 1 < n:
            max_count_result = max(max_count_result,vertical_swap(i, j))

        if j + 1 < n:
            max_count_result = max(max_count_result,horizontal_swap(i, j))

print(max_count_result)
