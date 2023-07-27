from input import input_xy

# 1. 좌표 입력
arr = input_xy.generate_arr_xy()
print(arr)
visited = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
print(visited)


# 2. dfs 탐색
def dfs(arr, visited, x, y):
    if visited[x][y] or arr[x][y] == 1:
        return
    visited[x][y] = 1
    _x, _y, x_, y_ = x - 1, y - 1, x + 1, y + 1

    if 0 <= x < len(arr) - 1:
        dfs(arr, visited, x_, y)
    if 0 < x < len(arr):
        dfs(arr, visited, _x, y)
    if 0 < y < len(arr[0]):
        dfs(arr, visited, x, _y)
    if 0 <= y < len(arr[0]) - 1:
        dfs(arr, visited, x, y_)


result = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if not arr[i][j] and not visited[i][j]:
            dfs(arr, visited, i, j)
            result += 1

# 3. 전체 그래프 개수 출력
print(result)
