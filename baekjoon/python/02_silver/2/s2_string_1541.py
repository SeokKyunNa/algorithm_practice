"""
silver2 1541
잃어버린 괄호
"""

def solution():
    exp = input()   # 입력받은 식
    first_minus = False # 첫 번째 마이너스(-) 기호인치 체크
    bracket = False # 열린 괄호 체크
    new_exp = ''    # 괄호를 포함한 수식
    zero_check = False  # 수의 시작이 0인지 체크

    for i in range(len(exp)):
        # 현재 숫자가 0일 때
        if exp[i] == '0':
            # 맨 처음 숫자가 0일 때
            if i==0:
                zero_check = True
                continue
            # 연산기호 다음의 숫자가 0일 때
            if i!=0 and exp[i-1] in ('-', '+'):
                zero_check = True
                continue
            # 이 전의 숫자들이 0일 때
            if zero_check:
                continue

        if exp[i] == '-':
            # 첫 번째 마이너스이면 닫는 괄호 필요 없음
            if not first_minus:
                first_minus = True
                new_exp += '-('
            else:
                new_exp += ')-('
            # 괄호가 열렸으므로 bracket 값을 True로 바꿔줌
            bracket = True
        elif exp[i] == '+':
            new_exp += '+'
        else:
            new_exp += exp[i]
            zero_check = False

    # 수식에서 괄호가 열린 채로 끝나면 안되므로 bracket 체크 후 닫아주기
    if bracket:
        new_exp += ')'

    # eval 함수로 수식을 계산하고 값을 return
    return eval(new_exp)

if __name__ == '__main__':
    print(solution())