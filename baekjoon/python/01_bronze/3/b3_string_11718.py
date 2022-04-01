"""
bronze1 11717
그대로 출력하기
"""

import sys
input = sys.stdin.readline

def solution():
    result = ''
    while True:
        # 입력
        curr = input().rstrip()
        # 입력받은 문자가 공백이면 break
        if curr == '':
            break

        # result에 입력을 누적 시킴
        result = result + curr + '\n'
    
    return result


if __name__ == '__main__':
    print(solution())

