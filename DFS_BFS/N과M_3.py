N, M = map(int, input().split())

d = [i + 1 for i in range(N)]


def backtrack(i, result):
    if len(result) >= M:

        return

    result.append(d[i])

    for j in range(N):
        backtrack(j, result)
    if len(result) == M:
        print(" ".join(map(str, result)))
    result.pop()
    return


for i in range(N):
    backtrack(i, [])
