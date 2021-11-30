"""
simple_linked_list.py: Class of Simple Linked list()
단순연결리스트: 1개의 링크로 연결된 연결리스트, 마지막 노드의 링크값=NULL/None

- __init__: initialization of parameters (head, size)  # head: 헤더노드
- size_: print size of linked list
- isEmpty: check whether size == 0
- insert_front: insert element at the front of linked list
- insert_after: insert element at specific position
- delete_: delete element at specific position
- print_list: print total elements of linked list

- requirements: Node class (노드 생성)
"""

'''
[특정 위치에 삽입]
insert_node(L, before, new)
if L = NULL
    then L <- new
else
    new_link <- before_link
    before_link <- new
'''

'''
[특정 위치에 삭제]
remove_node(L, before, removed)
if L != NULL
    then
        before_link <- removed_link
        destroy(removed)
'''


# 연결리스트 구성요소인 노드 생성 클래스 (item=데이터/항목, link=주소/링크)
class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Simple_Linked:
    def __init__(self):
        self.head = None
        self.size = 0

    def size_(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    # 연결리스트 맨 앞에 추가
    def insert_front(self, item):
        if self.isEmpty():  # 비어있는 경우, 새로운 헤더노드로 생성
            self.head = Node(item, None)
        else:
            self.head = Node(item, self.head)
            self.size += 1

    # 연결리스트 특정 위치에 추가
    def insert_after(self, item, pos):
        if pos == 0:  # 맨 앞에 추가하는 경우
            self.insert_front(item)
        elif self.size + 1 >= pos:  # 특정 위치에 추가하는 경우
            header = self.head
            for _ in range(1, pos):
                header = header.next
            new = Node(item, header.next)
            header.next = new
            self.size += 1
        else:
            print(f'Unable to add to position {pos}')

    # 연결리스트 특정 위치에 삭제
    def delete_(self, pos):
        if pos < 0 or self.size < pos:
            return None
        elif pos == 1:  # 삭제하는 노드가 헤더노드인 경우
            self.head = self.head.next
        else:
            header = self.head
            for _ in range(1, pos-1):
                header = header.next
            header.next = header.next.next
            self.size -= 1

    # 연결리스트 내 모든 요소 반환
    def print_list(self):
        header = self.head
        while header:
            if header.next is not None:
                print(f'{header.item} -> ', end=' ')
            else:
                print(header.item)
            header = header.next


if __name__ == '__main__':
    sll = Simple_Linked()
    sll.insert_front('my')  # insert_front: 마지막 경우만 유효함
    # sll.insert_front('was') 하면 앞서 my 무효처리됨.
    sll.insert_after('name', 1)
    sll.insert_after('is', 2)
    sll.insert_after('zoey', 3)
    sll.print_list()