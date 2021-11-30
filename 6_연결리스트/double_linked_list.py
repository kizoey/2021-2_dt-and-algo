"""
double_linked_list.py: Class of Double Linked list()
이중연결리스트: 2개의 노드인 선행노드와 후속노드를 이용해 연결된 연결리스트

- __init__: initialization of parameters (head, tail, size)
- isEmpty: check whether size == 0
- insert_before: insert element at specific position (before 노드 기준)
- insert_after: insert element at specific position (after 노드 기준)
- delete_: delete element at specific position
- print_list: print total elements of linked list
- search_item: search item at specific position (경로 탐색해서 p.item == item 일 때 위치 반환)

- requirements: Node class (노드 생성)
"""

'''
[before 노드 기준 삽입]
void insert_nide(DlistNode * before, DlistNode * new_node)
{
    new_node -> llink = before
    new_node -> rlink = before -> rlink
    before -> rlink -> llink = new_node
    before -> rlink = new_node
}
'''

'''
[after 노드 기준 삽입]
void inert_nide(DlistNode * after, DListNode * new_node)
{
    new_node -> rlink = after
    new_node -> llink = after -> llink
    after -> llink -> rlink = new_node
    after -> llink = new_node
}
'''

'''
[데이터 삭제]
void dremove_node(DlistNode * phead_node, DlistNode * removed)
{
    removed -> llink -> rlink = removed -> rlink
    removed -> rlink -> llink = removed -> llink
}
'''


# 연결리스트 구성요소인 노드 생성 클래스 (item=데이터/항목, link=주소/링크)
class Node:
    def __init__(self, item, llink, rlink):
        self.item = item
        self.before = llink
        self.next = rlink


class Double_Linked:
    def __init__(self):
        self.head = Node(None, None, None)  # 선행 노드/데이터/후속 노드
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    # before 노드 기준 데이터 삽입
    def insert_before(self, pos, item):
        tmp = pos.before
        node = Node(item, tmp, pos)
        pos.before = node
        tmp.next = node
        self.size += 1

    # after 노드 기준 데이터 삽입
    def insert_after(self, pos, item):
        tmp = pos.next
        node = Node(item, pos, tmp)
        tmp.before = node
        pos.next = node
        self.size += 1

    # 연결리스트 특정 위치에 삭제
    def delete_(self, x):
        bf = x.before
        nx = x.next
        bf.next = nx
        nx.before = bf
        self.size -= 1
        return x.item

    # 연결리스트 내 모든 요소 반환
    def print_list(self):
        if self.isEmpty():
            print('List is empty.')
        else:
            tmp = self.head.next
            while tmp != self.tail:
                if tmp.next != self.tail:
                    print(tmp.item, '<->', end=' ')
                else:
                    print(tmp.item)
                tmp = tmp.next

    # 특정 아이템의 위치 삭제
    def search_item(self, item):
        if self.isEmpty():
            print('List is empty.')
        else:
            tmp = self.head
            for i in range(self.size+1):
                if item == tmp.item:
                    return tmp
                tmp = tmp.next
            return None


if __name__ == '__main__':
    dll = Double_Linked()
    dll.insert_before(dll.tail, 'zoey')
    dll.print_list()
    dll.insert_before(dll.tail.before, 'name')
    dll.insert_after(dll.head.next, 'is')
    dll.print_list()
    dll.delete_(dll.head.next.next)  # name is
    if dll.search_item('name') is not None:
        dll.insert_after(dll.search_item('name'), 'zoey')
