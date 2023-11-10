import sys


def dfs(index, depth, min_cost, start):
    if depth == n:
        if cost[index][start] != 0:
            min_cost += cost[index][start]
            result.append(min_cost)
            min_cost -= cost[index][start]

        return

    for i in range(n):
        if not visited[i]:
            if cost[index][i] != 0:
                visited[index] = True
                min_cost += cost[index][i]
                dfs(i, depth + 1, min_cost, start)
                min_cost -= cost[index][i]
                visited[index] = False


n = int(input())
cost = []
visited = [False] * n
result = []

for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    dfs(i, 1, 0, i)


print(min(result))
