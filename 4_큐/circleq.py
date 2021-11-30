"""
circleq.py: Class of Circle Queue()
FIFO: 선입선출, 먼저 들어간 것이 먼저 나오는 구조

- __init__: initialization of parameters (size, data, front, rear)
- isFull, isEmpty: 큐의 포화상태/공백상태 확인 (포화: front % M == (rear+1) % M, 공백: front == rear)
- clear: empty all front and rear
- enqueue: insert element into queue at rear
- dequeue: delete element of queue at front
- peak: return top element
- display: return all elements in queue
"""


class CircleQ:
    def __init__(self):
        self.size = size
        self.data = [None]*self.size  # initialize with None
        self.front = 0
        self.rear = 0

    def isFull(self):
        return self.front == (self.rear+1) % self.size  # 나머지 계산

    def isEmpty(self):
        return self.front == self.rear

    def clear(self):
        self. front = self.rear

    # 큐에 데이터 삽입 (후단, rear 사용)
    def enqueue(self, value):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = value

    # 큐에 데이터 삭제 (전단, front 사용)
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.data[self.front] = None

    # 가장 최근 데이터 반환
    def peak(self):
        if not self.isEmpty():
            return self.data[(self.front + 1) % self.size]

    def display(self):
        print(self.data)


if __name__ == '__main__':
    size = int(input('Enter size of Circle Q: '))
    circleq = CircleQ()
    circleq.enqueue(1)
    circleq.enqueue(10)
    circleq.dequeue()
    circleq.dequeue()
    circleq.enqueue(40)
    circleq.enqueue(80)
    circleq.enqueue(120)
    circleq.display()
    print(f'front: {circleq.front}, rear: {circleq.rear}')