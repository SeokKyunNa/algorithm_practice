"""
bronze1 1032
명령 프롬프트
"""

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    words = []
    searching_word = ''

    # 단어 입력
    for _ in range(N):
        words.append(input().rstrip())

    # 모든 단어 돌면서 같읕 자리에 있는 문자 확인
    # 같은 자리의 문자들을 set으로 묶었을 때 1개이면 그대로, 2개 이상이면 '?' 입력

    # 단어의 길이만큼 순회
    for i in range(len(words[0])):
        tmp = []
        # 모든 단어 순회
        for j in range(len(words)):
            tmp.append(words[j][i])
        if len(set(tmp)) == 1:
            searching_word += words[j][i]
        else:
            searching_word += '?'

    return searching_word

if __name__ == '__main__':
    print(solution())