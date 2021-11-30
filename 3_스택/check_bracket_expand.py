"""
check_bracket_norm.py: check for matching brackets (for all brackets, (), {}, [])

- input: expression (str)
- output: stack (stack)
- purpose: check whether the input expression has matching open brackets (same number of open/close brackets)
"""


def check_brackets_expand(text: str):
    stack = []
    for i in text:
        open_brk = '({['
        close_brk = ')}]'
        if i in open_brk:  # 열린 괄호라면
            stack.append(i)
        elif i in close_brk:
            if open_brk.find(stack.pop) != close_brk.find():  # matching bracket 아닌경우
                return False
    if not stack:  # empty stack, True 반환
        return True
    else:
        return True


'''
[확장형 괄호 검사]
step 1. 시작, 괄호가 포함된 수식/문자열 입력
step 2. 열린 괄호 ('(','{','['가 맞는지 확인)
    step 2-1. 열린 괄호가 맞다면 스택에 push
step 3. 열린 괄호가 아니라면 닫힌 괄호 (')','}',']'가 맞는 지 확인)
    step 3-1. 닫힌 괄호가 맞다면 스택에 저장된 열린 괄호 pop
    step 3-2. pop 괄호와 현재 괄호 비교, matching bracket 확인
    step 3-3. 틀리면 오류 출력
step 4. 닫힌 괄호가 아니고 step 3-2.에서 열린 괄호-닫힌 괄호 쌍이라면 스택에 남아있는 괄호 여부 확인, 끝
'''
if __name__ == '__main__':
    text = input('Input Expression: ')
    print(f'Check for brackets: {check_brackets_expand(text)}')
