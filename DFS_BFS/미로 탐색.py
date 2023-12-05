import sys
from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs(x, y):
    # 상하좌우 이동 좌표 설정
    bx = [1, -1, 0, 0]
    by = [0, 0, 1, -1]

    # 시작점 좌표를 큐에 삽입
    queue = deque()
    queue.append((x, y))

    while queue:
        # 현재 위치
        x, y = queue.popleft()

        # 네 방향에 대해 확인
        for i in range(4):
            nx = x + bx[i]
            ny = y + by[i]

            # 범위 밖 좌표는 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 막힌 곳 무시
            if maze[nx][ny] == 0:
                continue

            # 이동 가능한 경우, 현재까지의 거리 + 1 후 해당 좌표를 현재 좌표로 최신화
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]


print(bfs(0, 0))
