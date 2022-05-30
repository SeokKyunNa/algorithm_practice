"""
단어의 개수 세기
"""
import sys
input = sys.stdin.readline

def solution():
    substring = input().strip()

    if len(substring) == 0:
        return 0

    while '  ' in substring:
        substring = substring.replace('  ', ' ')

    count = 1
    for char in substring:
        if char == ' ':
            count += 1

    return count

if __name__ == '__main__':
    print(solution())