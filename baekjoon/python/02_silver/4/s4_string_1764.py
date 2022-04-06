"""
silver4 1764
듣보잡
"""

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    nolisten_set = set()
    nosee_set = set()

    # 듣도 못한 사람 입력
    for _ in range(N):
        nolisten_set.add(input().rstrip())

    # 보도 못한 사람 입력
    for _ in range(M):
        nosee_set.add(input().rstrip())

    # 듣도 못한 set과 보도 못한 set을 비교하여 두 set에 모두 포함된 값만 list에 저장
    noall_list = list()
    # for name in nolisten_set:
    #     if name in nosee_set:
    #         noall_list.append(name)

    # 논리 연산자로 두 set 비교 가능!
    noall_list = list(nolisten_set & nosee_set)

    # 리스트 정렬
    noall_list.sort()

    # 출력
    print(len(noall_list))
    for name in noall_list:
        print(name)

if __name__ == '__main__':
    solution()