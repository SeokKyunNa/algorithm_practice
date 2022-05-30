"""
의좋은 형제
"""
import sys
input = sys.stdin.readline

def solution():
    jinwoo, sunwoo = map(int, input().split())
    days = int(input())

    for day in range(1, days+1):
        if day%2 == 0:  # 선우가 주는 날
            if sunwoo%2 != 0:   # 홀수일 때
                jinwoo += 1
            jinwoo += sunwoo//2
            sunwoo //= 2
        else:   # 진우가 주는 날
            if jinwoo%2 != 0:   # 홀수일 때
                sunwoo += 1
            sunwoo += jinwoo//2
            jinwoo //= 2

    return jinwoo, sunwoo

if __name__ == '__main__':
    result = solution()
    print(result[0], result[1])