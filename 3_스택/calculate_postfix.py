"""
calculate_postfix.py: calculation of postfix expression

- input: expression (str), 후위표현식
- output: integer (int)
- requirements: Simple_Linked class
"""


class Stack:
    # class 수행시 __init__ 함수는 자동으로 시행된다. (여기서 파라미터 data, size 정의됨.)
    def __init__(self, size):
        self.data = []
        self.size = size

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.size

    def push(self, value):
        if not self.isFull():
            self.data.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]


'''
스택 s를 생성하고 초기화
for 항목 in 후위표기식
    do if (항목이 피연산자이면)
        push(s, item)
    if (항목이 연산자 op 이면)
        then second <- pop(s)
            first <- pop(s)
                result <- first op second (op는 +=*/ 중에 하나)
                push(s, result)
final_result <- pop(s)
'''


# 각 연산자별로 피연산자 스택에서 pop 한 뒤 시행, 결과값 다시 스택에 push
def postfix(expression):
    stack = Stack(20)
    for element in expression:
        if element == '+':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(op1 + op2)
        elif element == '-':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(op1 - op2)
        elif element == '*':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(op1 * op2)
        elif element == '/':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push( op1 / op2)
        else:
            stack.push(int(element))
    answer = stack.pop()
    return answer


'''
[후위표현식 계산 알고리즘]
step 1. 수식을 왼쪽에서 오른쪽으로 스캔
step 2. 피연산자이면 스택에 push
step 3. 연산자이면 연산에 필요한 수만큼의 피연산자를 스택에서 꺼내서 연산 실행
step 4. 연산 결과 다시 스택에 push
'''
if __name__ == '__main__':
    postfix_exp = input('Input Expression: ')
    print(f'Postfix Calculation: {postfix(postfix_exp)}')
