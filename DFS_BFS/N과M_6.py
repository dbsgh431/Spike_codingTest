N, M = map(int, input().split())

N_input = list(map(int, input().split()))

# 사전 순 출력을 위해 오름차순 정렬
N_input = sorted(N_input)


result = []

# 백트래킹
def bactrack(i, n_input : list):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for j in range(i, len(n_input)):
        result.append(n_input[j])
        n_input.pop(j)
        bactrack(j, n_input)
        n_input.insert(j, result.pop())

    return


# run
bactrack(0, N_input)