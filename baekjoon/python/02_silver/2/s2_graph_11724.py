"""
silver2 11724
연결 요소의 개수
"""

from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

for i in range(1, N+1):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)
