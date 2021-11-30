"""
infix_to_postfix.py: change format of infix expression to postfix expression, 중위표현식을 후위표현식으로
1. 중위표기식 & 후위표기식: 피연산자의 순서 동일, 연산자들의 순서(우선순위) 동일하지 않음.
   따라서, 연산자만 스택에 push 한 뒤에 저장해서 사용한다. 피연산자는 스택을 거치지 않고 그대로 출력.
2. 후위표기식: 괄호 없이도 계산 순서 일정, 이미 우선순위 내포

- input: expression (str), 중위표현식
- output: expression (str), 후위표현식
- purpose: change the format of expression from infix to postfix to allow computer operate easily

- requirements: Simple_Linked class, precedence (연산자간 우선순위)
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


# input: operator, output: priority operator
def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1


def infix_to_postfix(infix):
    stack = Stack(20)  # Simple_Linked 클래스 이용해서 20 사이즈의 스택 인스턴스 생성
    result = []
    for i in infix:
        if i in '(':
            stack.push('(')
        elif i in ')':
            while not stack.isEmpty():
                tmp = stack.pop()
                if tmp == '(':  # 열린 괄호 나타날때까지 스택에서 전부 pop
                    break
                else:  # 열린 괄호 제외한 나머지는 바로 result 리스트에 append
                    result.append(tmp)
        elif i in '+-*/':  # 연산자인 경우, 스택의 top element 반환
            while not stack.isEmpty():
                tmp = stack.peek()
                if precedence(i) <= precedence(tmp):  # top element 우선순위 비교시 더 낮으면 연산자 result append
                    result.append(tmp)
                    stack.pop()
                else:
                    break
            stack.push(i)  # 우선순위 더 낮은 현재 연산자 스택에 push
        else:  # 피연산자인 경우 바로 result append
            result.append(i)
    while not stack.isEmpty():  # 비어있지 않으면 스택에 남아있는 것들 모두 pop, result append
        result.append(stack.pop())
    return result


'''
[중위표현식에서 후위표현식 변환 알고리즘]
step 1. 피연산자인 경우, 바로 출력
step 2. 연산자인 경우 스택에 push, 스택의 맨 위 연산자보다 우선순위가 같거나 낮은 연산자가 나오면 스택에서 해당 연산자 pop
        (즉, 스택의 top 요소 연산자보다 낮은 연산자가 들어오면 기존 연산자 pop, 높은 연산자가 들어오면 높은 연산자 그 위로 push, top += 1)
step 3. 괄호가 입력된 연산 처리
    step 3-1. 열린 괄호 = 우선순위 가장 높음, 스택의 순위와 관계없이 항상 push
    step 3-2. 닫힌 괄호 = 스택에서 열린 괄호 위에 쌓여있는 모든 연산자 pop, 열린 괄호와 만나면 같이 사라짐
'''
if __name__ == '__main__':
    infix_exp = input('Input Expression: ')
    print(f'Infix to Postfix: {infix_to_postfix(infix_exp)}')
