"""
silver3 9372
상근이의 여행
"""

from collections import deque
import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    print(N-1)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solution()