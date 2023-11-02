N, M = map(int, input().split())

result = []


def backtrack(i):
    if len(result) >= M:
        print(" ".join(map(str, result)))
        return

    for j in range(i, N + 1):
        result.append(j)
        backtrack(j)
        result.pop()
    return


backtrack(1)