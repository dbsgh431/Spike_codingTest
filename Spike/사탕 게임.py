import sys
import copy


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


def check_vertical(j, n_list):

    stack = [n_list[0][j]]
    count = 1
    stack_count = [0]
    for k in range(1, len(n_list)):
        if stack[-1] == n_list[k][j]:
            count += 1
        else:
            stack_count[0] = max(stack_count[0], count)
            count = 1
            stack.clear()
        stack.append(n_list[k][j])
    stack_count[0] = max(stack_count[0], count)
    return max(stack_count)


def check_horizontal(i, n_list):

    stack = [n_list[i][0]]
    count = 1
    stack_count = [0]
    for k in range(1, len(n_list)):
        if stack[-1] == n_list[i][k]:
            count += 1
        else:
            stack_count[0] = max(stack_count[0], count)
            count = 1
            stack.clear()
        stack.append(n_list[i][k])
    stack_count[0] = max(stack_count[0], count)
    return max(stack_count)


def horizontal_swap(i, j, n_list):
    n_list[i][j], n_list[i][j + 1] = n_list[i][j + 1], n_list[i][j]

    result = max(check_vertical(j, n_list), check_vertical(j + 1, n_list), check_horizontal(j + 1, n_list), check_horizontal(j, n_list))

    return result


def vertical_swap(i, j, n_list):
    n_list[i][j], n_list[i + 1][j] = n_list[i + 1][j], n_list[i][j]
    result = max(check_horizontal(i, n_list), check_horizontal(i + 1, n_list), check_vertical(i, n_list), check_vertical(i + 1, n_list))
    return result


max_count = -1
for i in range(len(n_list) - 1):
    for j in range(len(n_list) - 1):
        max_count = max(max_count, horizontal_swap(i, j, copy.deepcopy(n_list)),
                        vertical_swap(i, j, copy.deepcopy(n_list)),
                        check_vertical(j, copy.deepcopy(n_list)), check_horizontal(i, copy.deepcopy(n_list)))
    max_count = max(max_count,
                    vertical_swap(i, len(n_list) - 1, copy.deepcopy(n_list))
                    )

max_count = max(max_count,
                    check_vertical(len(n_list) - 1, copy.deepcopy(n_list)), check_horizontal(len(n_list) - 1, copy.deepcopy(n_list))
                    )



print(max_count)
