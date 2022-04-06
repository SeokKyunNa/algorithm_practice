"""
bronze2 10953
A+B -6
"""
import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for i in range(T):
        print(sum(map(int, input().split(','))))

if __name__ == '__main__':
    solution()