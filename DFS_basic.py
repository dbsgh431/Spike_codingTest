# DFS 함수 정의
def dfs(graph, v, visited):
    # 방문 처리
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 인덱스(노드)별 연결 정보를 가지는 인접 리스트
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

dfs(graph, 1, visited)