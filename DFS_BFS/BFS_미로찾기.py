from collections import deque

from input import input_xy

# 1. 좌표 입력

arr = input_xy.generate_arr_xy()
print(arr)

visited = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
print(visited)


# 2. bfs 탐색
def bfs(x, y, visited, distance):
    queue = deque([[x, y, distance]])

    while queue:
        loc = queue.popleft()
        if loc[0] < 0 or loc[0] > len(arr) - 1 or loc[1] < 0 or loc[1] > len(arr[0]) - 1:
            pass
        else:
            if not visited[loc[0]][loc[1]] and arr[loc[0]][loc[1]] != 0:
                visited[loc[0]][loc[1]] = True

                loc[2] += 1
                arr[loc[0]][loc[1]] = loc[2]

                queue.append([loc[0] + 1, loc[1], loc[2]])
                queue.append([loc[0] - 1, loc[1], loc[2]])
                queue.append([loc[0], loc[1] + 1, loc[2]])
                queue.append([loc[0], loc[1] - 1, loc[2]])
                
    return arr[-1][-1]


print(bfs(0, 0, visited, 0))
