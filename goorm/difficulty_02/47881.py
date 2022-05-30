"""
근묵자흑
"""
import sys
import math
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    n_list = list(map(int, input().split()))

    if len(n_list) < K:
        return 1

    count = ((N - K) / (K - 1)) + 1

    return math.ceil(count)

if __name__ == '__main__':
    print(solution())