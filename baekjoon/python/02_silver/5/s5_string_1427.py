"""
silver5 1427
소트인사이드
"""

def solution():
    # 입력받은 값을 리스트로 나눔
    num = list(map(int, input()))
    # 내림차순 정렬
    num.sort(reverse=True)
    # 정렬된 리스트를 이어붙임
    result = ''.join(map(str, num))

    return result

if __name__ == '__main__':
    print(solution())
