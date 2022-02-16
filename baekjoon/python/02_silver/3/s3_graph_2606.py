"""
silver3 2606
바이러스
"""

from collections import deque
import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    dq = deque()
    dq.append(1)
    visited[1] = True
    num = 0

    while dq:
        x = dq.popleft()
        for next in graph[x]:
            if visited[next]:
                continue
            dq.append(next)
            visited[next] = True
            num += 1
    
    return num

if __name__ == '__main__':
    print(solution())
                

