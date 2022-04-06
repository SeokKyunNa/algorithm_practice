"""
bronze2 10808
알파벳 개수
"""

def solution():
    # key로 a~z를 갖고, value는 모두 0인 dictionary를 만듦
    alpha_dict = dict()
    for i in range(97, 123):
        alpha_dict[chr(i)] = 0

    # 입력 받고 각 알파벳의 개수 누적 계산
    word = input()
    for c in word:
        alpha_dict[c] += 1

    # dictionary의 value 출력
    for value in alpha_dict.values():
        print(value, end=' ')

if __name__ == '__main__':
    solution()