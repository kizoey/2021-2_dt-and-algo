"""
queue_library.py: Class of Queue() using queue library
- import queue: 큐 라이브러리 적재
- queue.Queue(maxsize=n): maxsize n 큐 생성
- queue.full(): isFull, 큐의 포화상태 확인 (front % M == (rear+1) % M)
- queue.put(i): 큐에 i 요소 후단에서 enqueue
- queue.empty(): isEmpty, 큐의 공백상태 확인 (front == rear)
- queue.get(): 큐 전단에서 dequeue
"""

import queue


if __name__ == '__main__':
    queue_lib = queue.Queue(maxsize=8)
    for i in range(1, 15):
        if not queue_lib.full():
            queue_lib.put(i)  # enqueue = put

    for _ in range(1, 10):
        if not queue_lib.empty():
            print(f'Queue: {queue_lib.get()}', end = ' ')  # dequeue = get
    print()