"""
circledeque.py: Class of Circle Deque()
- 전단과 후단에서 모두 삽입/삭제가 자유로운 구조 (큐의 구조와 스택의 기능들)
- circleq 클래스를 상속한 뒤에 몇몇 원형덱의 기능을 추가해 사용한다.

- super().__init__: initialization of parameters of CircleQ class (super.은 자식클래스에서 부모클래스 불러오는 경우)
- addRear: insert element at rear (rear = (rear+1) % M)
- addFront: insert element at front (front = (front-1+M) % M)  - 원형덱에서 새롭게 추가된 기능 (반시계방향 회전)
- deleteRear: delete element at rear (rear =  (rear-1+M) % M)  - 원형덱에서 새롭게 추가된 기능 (반시계방향 회전)
- deleteFront: delete element at front (front = (front+1) % M)

- requirements: CircleQ class
"""


class CircleQ:
    def __init__(self, size):
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

    def enqueue(self, value):  # rear 데이터 삽입
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = value

    def dequeue(self):  # front 데이터 삭제
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.data[self.front] = None

    def peak(self):
        if not self.isEmpty():
            return self.data[(self.front + 1) % self.size]

    def display(self):
        print(self.data)


# Circle Queue 클래스 상속한 원형덱
class CircleDeque(CircleQ):
    def __init__(self, size):
        super().__init__(size)  # CircleQ class size 파라미터 생성

    def addRear(self, data):
        self.enqueue(data)

    # 원형덱의 기능: 전단에서 데이터 삽입
    def addFront(self, data):
        if self.isFull():
            return print('Simple_Linked is full. Not able to add.')
        else:
            self.data[self.front] = data
            self.front = (self.front-1+self.size) % self.size

    # 원형덱의 기능: 후단에서 데이터 삭제
    def deleteRear(self):
        if self.isEmpty():
            return print('Simple_Linked is empty. Not able to delete.')
        else:
            tmp = self.data[self.rear]   # 삭제할 요소
            self.data[self.rear] = None  # 삭제
            self.rear = (self.rear-1+self.size) % self.size
        return tmp  # 삭제한 요소 반환

    def deleteFront(self):
        self.dequeue()


if __name__ == '__main__':
    deq = CircleDeque(8)  # 8 사이즈의 원형덱 생성
    tmp = 10
    for i in range(5):  # 10~50까지 데이터 삽입
        deq.addRear(tmp)
        tmp += 10
    deq.deleteRear()
    deq.addFront(100)
    deq.addFront(200)
    print(f'Front: {deq.front}, Rear: {deq.rear}')
    print(f'Circular deque data: {deq.data}')
