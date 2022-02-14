"""
gold5 5430
AC
"""

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    p = input().rstrip()
    n = int(input())
    num_deque = deque(input().rstrip().strip('[]').split(','))
    r_flag = 1  # 1: 순방향, 0: 역방향

    for order in p:
        if order == 'R':
            r_flag = 1 - r_flag
        else:
            if not num_deque or num_deque[0]=='':
                print('error')
                return
            
            if r_flag == 1:
                num_deque.popleft()
            else:
                num_deque.pop()

    if r_flag == 0:
        num_deque.reverse()

    print('[' + ','.join(num_deque) + ']')

def main():
    T = int(input())
    for _ in range(T):
        solution()


if __name__ == '__main__':
    main()
