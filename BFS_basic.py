from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 선입선출을 위한 큐 정의
    queue = deque([start])

    visited[start] = True

    # 큐에 탐색할 원소가 없을 때 까지
    while queue:
        # 탐색할 노드를 큐에서 반출
        v = queue.popleft()
        print(v, end=' ')

        # 방문하지 않은 노드를 큐에 push
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)