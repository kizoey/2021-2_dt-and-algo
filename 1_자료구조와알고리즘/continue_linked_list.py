"""
continue_linked_list.py: create linked list and find certain item within linked list, 연결형 연결리스트

- create: 정해진 개수만큼 연결형 리스트에 데이터 생성
- search: 연결형 리스트에서 특정 데이터 찾기

- requirements: Node class (노드 생성)
"""


class Node:
    def __init__(self, val, link):
        self.data = val
        self.link = link


class Continue_Linked:
    # Continue_Linked 클래스 실행시 자동으로 실행되는 부분
    def __init__(self):  # __init__ 함수 안에 self 넣어줌으로써 할당하는 변수의 정보를 담도록 한다.
        self.head = None
        self.size = 0

    # 정해진 개수만큼 연결리스트에 데이터 생성
    def create(self, data):
        self.head = Node(data[0], None)
        self.size = len(data)
        header = self.head
        for i in range(1, len(data)):
            s = Node(data[i], None)
            header.link = s
            header = s

    # 연결 리스트에서 데이터 찾기
    def search(self, value):
        header = self.head
        for _ in range(self.size):
            if header is None:  # 데이터가 없는 경우
                return f'No Data.'
            else:
                if header.data == value:  # 데이터가 헤더노드인 경우 바로 찾기, 아니면 순환문 돌기
                    return f'Found {value}'
            header = header.link
        return f'{value} Not Found.'  # 데이터가 연결형 리스트에 없는 경우


if __name__ == '__main__':
    data = ['my', 'name', 'is', 'zoey']
    cll = Continue_Linked()
    cll.create(data)
    print(cll.search('zoey'), '\n', cll.search('dayeon'))
