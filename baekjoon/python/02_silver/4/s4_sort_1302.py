"""
silver4 1302
베스트셀러
"""

import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input())
    books = defaultdict(int)
    bestsellers = []

    # N개의 책 제목 입력
    for i in range(N):
        book = input().rstrip()
        books[book] += 1

    # 가장 많이 팔린 개수 확인
    maximum = max(books.values())
    
    # maximum과 같은 value를 갖는 key 따로 저장
    for key, value in books.items():
        if value == maximum:
            bestsellers.append(key)

    # 이름순으로 정렬 후 제일 앞의 값 출력
    print(sorted(bestsellers)[0])

if __name__ == '__main__':
    solution()
