from input import input_xy

# 1. 좌표 입력
arr = input_xy.generate_arr_xy()
print(arr)


# 2. dfs 탐색
def dfs(x, y):
    if x < 0 or x > len(arr) - 1 or y < 0 or y > len(arr[0]) - 1:
        return False
    if not arr[x][y]:
        arr[x][y] = 1
        _x, _y, x_, y_ = x - 1, y - 1, x + 1, y + 1

        dfs(x_, y)
        dfs(_x, y)
        dfs(x, _y)
        dfs(x, y_)
        return True
    return False


result = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if not arr[i][j]:
            if dfs(i, j):
                result += 1

# 3. 전체 그래프 개수 출력
print(result)
