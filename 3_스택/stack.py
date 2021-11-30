"""
stack.py: Class of Simple_Linked()
LIFO: 후입선출, 나중에 들어간 것이 먼저 나오는 구조

- __init__: initialization of parameters (string, List[int])
- push: insert element into stack
- pop: pop element out of stack
- empty: check string == []
- top: return top element of stack, if None, return empty message
"""


class Stack:
    def __init__(self):
        self.string = []

    def push(self, item):
        self.string.append(item)

    def pop(self):
        if len(self.string) != 0:  # 스택이 비어있지 않은 경우
            item = self.string.pop(-1)  # pop top element
            return item
        else:
            print('Simple_Linked is empty. Nothing to pop.')

    def empty(self):
        if not self.string:
            return True
        else:
            return False

    def top(self):
        if len(self.string) != 0:
            return self.string[-1]  # return top element
        else:
            print('Simple_Linked is empty. No top element.')


'''
[문자열 역순 출력]
step 1. 시작, 문자열 입력
step 2. 입력된 문자열 스택 구조에 push
step 3. 스택에 저장된 문자들 pop
step 4. pop 되는 값들 출력, 끝
'''
if __name__ == '__main__':
    stack_str = Stack()
    stack_str.push('A')
    stack_str.pop()
    stack_str.push('B')
    stack_str.push('C')
    stack_str.push('D')
    data = ''
    for i in range(len(stack_str.string)):
        data += stack_str.pop()
    print(data)