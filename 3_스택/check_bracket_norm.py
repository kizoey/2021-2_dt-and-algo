"""
check_bracket_norm.py: check for matching brackets (only for open brackets, ())

- input: expression (str)
- output: stack (stack)
- purpose: check whether the input expression has matching open brackets (same number of open/close brackets)
"""


def check_brackets_norm(text: str):
    stack = []
    for idx, exp in enumerate(text):
        # 열린 괄호 확인 (열린 괄호인 경우, 스택에 idx append)
        if exp == '(':
            stack.append(idx)
        # 닫힌 괄호 확인 (닫힌 괄호인 경우, 이미 있으면 열린 괄호 pop, 열린 괄호 아니면 닫힌 괄호 append
        elif exp == ')':
            if stack:
                stack.pop()
            else:
                stack.append(idx)
                return stack
        return stack


if __name__ == '__main__':
    text = input('Input Expression: ')
    print(f'Check for brackets: {check_brackets_norm(text)}')
