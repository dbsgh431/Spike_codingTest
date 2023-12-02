from collections import deque
import sys

m, n = map(int, input().split())

# 토마토 상태 저장
tomatos = []
for i in range(n):
    tomatos.append(list(map(int, sys.stdin.readline().rstrip().split())))

# bfs를 위한 deque, visited 정의
queue = deque()
visited = [[False for _ in range(m)] for _ in range(n)]

# 탐색 시작지점으로 1인 상태의 토마토가 있는 좌표를 큐에 삽입
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            queue.append((i, j))

# 이동 방향에 따른 좌표 변화값 저장
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = - 100
# bfs
while queue:
    # 익은 토마토의 좌표를 꺼내옴
    d = queue.popleft()
    x, y = d[0], d[1]
    # 방문 처리
    visited[x][y] = True
    # 네 방향에 대해서 탐색
    for i in range(4):
        kx = x + dx[i]
        ky = y + dy[i]

        # 상자를 넘어선 경우는 무시
        if kx < 0 or kx >= n or ky < 0 or ky >= m:
            continue
        # 토마토가 없거나 이미 방문한 칸은 무시
        if tomatos[kx][ky] == -1 or visited[kx][ky] == True:
            continue
        # 토마토가 있고, 방문가능한 경우 이전 칸까지의 날짜 수 + 1 후 큐에 해당 좌표 삽입
        if tomatos[kx][ky] == 0 and visited[kx][ky] == False:
            tomatos[kx][ky] = tomatos[x][y] + 1
            queue.append((kx, ky))

# 토마토가 있는 시작지점이 1이고(즉, 0일차가 1)
# 주변이 익을 때마다 + 1씩 되므로 가장 마지막의 값(최댓값)에 -1
answer = max(map(max, tomatos)) - 1

# 토마토가 모두 익지 못하는 상황 체크
for i in range(n):
    if answer == 0:
        break
    for j in range(m):
        if tomatos[i][j] == 0:
            answer = 0
            break

print(answer)