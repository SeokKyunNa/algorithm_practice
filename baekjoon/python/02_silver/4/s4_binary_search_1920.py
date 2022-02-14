"""
silver4 1920
수 찾기
"""

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = set(map(int, input().split()))

    M = int(input())
    check_num = list(map(int, input().split()))

    for num in check_num:
        if num in A:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solution()