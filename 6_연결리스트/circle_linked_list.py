"""
circle_linked_list.py: Class of Circle Linked list()
원형연결리스트: last node = header node

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
[처음 위치의 노드 삭제]
void delete_head(Clast * n)
{
	if(n -> last == NULL)
		return;
	else:
		temp = n -> last
		if(n -> last == n -> last -> next)
			n -> last = NULL
		else:
			n -> last = n -> last -> next
	free(temp)
}
'''

'''
[new_node 처음 위치에 추가]
void insert_head(Clast * n, ClistNode * new)
{
	if(n -> last == NULL)
		new -> next = new
		n -> last = new
	else:
		new -> next = n -> last
		n -> last = new
}
'''


# 연결리스트 구성요소인 노드 생성 클래스 (item=데이터/항목, link=주소/링크)
class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


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


class Circle_Linked(Double_Linked):  # Double_Linked, 이중 연결리스트에서 상속
    def __init__(self):
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    '''
    [처음 위치에 노드 추가]
    - 빈 리스트인지 아닌지 확인한 뒤, 빈 리스트이면 생성된 노드가 자기자신을 가리킬 수 있도록 함.
    - 빈 리스트가 아닌 경우, new_node 다음 정보를 last 삽입, last 다음으로 new_node 삽입
    '''
    def insert_head(self, item):
        new_node = Node(item, None)
        if self.isEmpty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
        self.size += 1

    def print_list(self):
        if self.isEmpty():
            print('Empty List.')
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, '->', end=' ')
                p = p.next
            print(p.item)


if __name__ == '__main__':
    cll = Circle_Linked()
    cll.insert_head('zoey')
    cll.insert_head('is')
    cll.insert_head('name')
    cll.insert_head('my')
    cll.print_list()
