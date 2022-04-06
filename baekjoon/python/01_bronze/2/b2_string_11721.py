"""
bronze2 11721
열 개씩 끊어서 출력하기
"""
import sys
input = sys.stdin.readline

def solution():
    line = input().rstrip()
    cnt = 0

    for c in line:
        cnt += 1
        print(c, end='')
        if cnt%10 == 0:
            print()

if __name__ == '__main__':
    solution()