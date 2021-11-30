"""
palindrome_linked_list.py: check whether it is palindrome, using linked list, 연결리스트 활용
- Runner 개념 활용
    - fast: 2단계씩 빠르게 이동해서 먼저 달려가 빠르게 끝까지 가는 것을 목표로 함. (원래 리스트 확인)
    - slow: 1단계씩 이동해서 역순 리스트 생성함. (역순 리스트, rev 확인)
- Single_Linked (단순연결리스트) 클래스에 linkedPalindrome 함수 추가
"""


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
            for _ in range(1, pos - 1):
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

    # 회문 여부 확인 (연결리스트 활용)
    def linkedPalindrome(self, head) -> bool:
        self.rev = None  # slow: 훑고 지나가는 역순 리스트 담을 리스트
        self.slow = self.fast = head

        while self.fast and self.fast.next:
            self.fast = self.fast.next.next  # fast: 2단계씩 이동
            self.rev, self.rev.next, self.slow = self.slow, self.rev, self.slow.next
        if self.fast:
            self.slow = self.slow.next  # fast 2단계씩 이동할 때 slow 1단계씩 이동
        while self.rev and self.rev.item == self.slow.item:
            self.slow, self.rev = self.slow.next, self.rev.next
        return not self.rev


if __name__ == '__main__':
    sll = Simple_Linked()
    sll.insert_front('1')
    sll.insert_after('2', -1)
    sll.insert_after('3', -1)
    sll.insert_after('2', -1)
    sll.insert_after('1', -1)
    sll.print_list()
    print(sll.linkedPalindrome(sll.head))
    # 1 -> 3 -> 2 -> 1 -> 2 (1 -> 3 -> 1, fast runner, slow runner)
