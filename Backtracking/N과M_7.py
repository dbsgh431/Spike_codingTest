N, M = map(int, input().split())

N_input = list(map(int, input().split()))

# 사전 순 출력을 위해 오름차순 정렬
N_input = sorted(N_input)


result = []

# 백트래킹
def bactrack(n_input : list):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for j in range(len(n_input)):
        result.append(n_input[j])
        bactrack(n_input)
        result.pop()
    return


# run
bactrack(N_input)