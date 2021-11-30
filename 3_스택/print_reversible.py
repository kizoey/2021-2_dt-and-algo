"""
print_reversible.py: print string in reversed order, 스택 연결리스트를 활용한 문자열 역순 출력

- __init__: initialization of parameters (top, size)
- isEmpty: check whether size == 0
- push_node: push node into stack
- pop_node: delete top node of stack

- requirements: Node class (노드 생성)
"""


class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Stack_Linked:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    # 노드 스택 연결리스트에 삽입
    def push_node(self, item):
        if self.isEmpty():  # 빈 스택 연결리스팅 경우, top 추가
            self.new_node = Node(item, None)
            self.top = self.new_node
        else:
            self.new_node = Node(item, self.top)
            self.top = self.new_node
        self.size += 1

    # 노드 스택 연결리스트에서 삭제
    def pop_node(self):
        if self.isEmpty():
            print('Empty stack.')
        else:
            tmp = self.top
            self.top = tmp.next
            self.size -= 1
        return tmp.item


'''
[문자열 역순 출력]
step 1. 시작, 문자열 입력
step 2. 입력된 문자열 스택에 push
step 3. 스택에 저장된 문자들 pop
step 4. pop 되는 값들 출력, 끝
'''
if __name__ == '__main__':
    stl = Stack_Linked()
    count = 0
    while True:
        stl.push_node(input('Enter character:'))
        count += 1
        if stl.new_node.item == '':  # enter 치면 break
            break
    for i in range(count):
        print(stl.pop_node(), end=' ')
