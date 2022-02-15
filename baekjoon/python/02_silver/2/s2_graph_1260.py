"""
silver2 1260
DFS와 BFS
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N+1):
    graph[i].sort()

dfs_visited = [False for _ in range(N+1)]
dfs_result = []

def dfs(x):
    dfs_visited[x] = True
    dfs_result.append(x)
    for next in graph[x]:
        if not dfs_visited[next]:
            dfs(next)

bfs_visited = [False for _ in range(N+1)]
bfs_result = []

def bfs():
    dq = deque()
    bfs_visited[V] = True
    bfs_result.append(V)
    dq.append(V)

    while dq:
        x = dq.popleft()
        for next in graph[x]:
            if bfs_visited[next]:
                continue
            bfs_visited[next] = True
            bfs_result.append(next)
            dq.append(next)


dfs(V)
print(*dfs_result)

bfs()
print(*bfs_result)