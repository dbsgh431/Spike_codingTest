N, M = map(int, input().split())

d = [i + 1 for i in range(N)]


def backtrack(i, depth, result):
    if depth == M:
        return ""

    else:
        result.append(d[i])
        depth += 1
        for j in range(i + 1, N):
            backtrack(j, depth, result)
        if depth == M:
            print(" ".join(map(str, result)))
        result.pop()
    return ""


for i in range(N - M + 1):
    backtrack(i, 0, [])
