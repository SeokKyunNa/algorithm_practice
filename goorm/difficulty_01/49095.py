"""
고장난 컴퓨터
"""
import sys
input = sys.stdin.readline

def solution():
    n, c = map(int, input().split())
    t_list = list(map(int, input().split()))

    count = 1
    before = 0

    for t in t_list[::-1]:
        if before == 0:
            before = t
            continue
            
        if before-t > c:
            break
        else:
            count += 1

        before = t

    return count

if __name__ == '__main__':
    print(solution())