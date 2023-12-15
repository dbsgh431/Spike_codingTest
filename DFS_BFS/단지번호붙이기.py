# 아이디어
# dfs, 이웃 여부를 확인하기 위해 상하좌우로 재귀호출
# 좌표를 넘어가거나, 집이 없는 경우 종료
# 집이 있고, 아직 방문하지 않은 경우에는 cnt + 1

n = int(input())
visited = [[0 for j in range(n)] for i in range(n + 1)]

houses = []
for i in range(n):
    houses.append(list(map(int, input())))


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if houses[x][y] == 1 and visited[x][y] == False:
        cnt += 1
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    else:
        return False


results = []
cnt = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            results.append(cnt)
            cnt = 0
results.sort()

print(len(results))
for result in results:
    print(result)
