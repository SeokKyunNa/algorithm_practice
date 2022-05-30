"""
막대기
"""
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    _list = list()

    for _ in range(N):
        _list.append(int(input()))

    cnt = 0
    maximum = 0
    for num in _list[::-1]:
        if maximum < num:
            maximum = num
            cnt += 1
        else:
            pass

    return cnt

if __name__ == '__main__':
    print(solution())