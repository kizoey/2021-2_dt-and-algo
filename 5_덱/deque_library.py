"""
deque_library.py: Class of Deque() using deque(collections) library
- from collections import deque: 덱 라이브러리 적재
- deque(): 덱 초기화
- deque.append(i): 덱에 i 요소 후단에서 삽입
- deque.appendleft(i): 덱에 i 요소 전단에서 삽입
- deque.pop(): 덱 후단에서 제거
- deque.popleft(): 덱 전단에서 제거
- deque.extend(list): 덱에 list 원소들 후단에서 삽입 (리스트 상태로 넣는 것이 아닌, 원소 상태로 넣음)
"""

from collections import deque


if __name__ == '__main__':
    dq = deque()
    print()
    item = ['my', 'name']
    dq.append('zoey')  # 후단에서 추가
    dq.appendleft('is')  # 전단에서 추가
    dq.appendleft(item)  # 전단에서 추가
    print(dq)  # my name is zoey
    dq.pop()  # 후단에서 삭제
    dq.popleft()  # 전단에서 삭제
    print(dq)
    item = ['guess', 'what']
    dq.extend(item)
    print(dq)