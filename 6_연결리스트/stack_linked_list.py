"""
stack_linked_list.py: create stack linked list, 스택 연결리스트 (연결된 리스트)

- __init__: initialization of parameters (last, size)
- push: insert element into stack linked list
- pop: delete top element from stack linked list
- print_stack: print total elements of stack linked list

- requirements: Node class (노드 생성), Double_Linked
"""


class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Stack_Linked:
    def __init__(self):
        self.top = None
        self.size = 0

    # 데이터 스택 연결리스트에 삽입
    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    # 데이터 스택 연결리스트에서 삭제
    def pop(self):
        if self.size != 0:
            tmp = self.top.item  # 맨 위 원소 확인하고 싶은 경우에만
            self.top = self.top.next
            self.size -= 1
        return tmp

    # 현재 스택 내 원소 확인
    def print_stack(self):
        print('top ->', end=' ')
        top_element = self.top
        while top_element:
            if top_element.next is not None:
                print(top_element.item, '->', end=' ')
            else:
                print(top_element.item, end=' ')
            top_element = top_element.next
        print()


if __name__ == '__main__':
    stl = Stack_Linked()
    stl.push('zoey')
    stl.push('is')
    stl.push('name')
    stl.push('my')
    stl.push('hi')
    stl.pop()
    stl.print_stack()
