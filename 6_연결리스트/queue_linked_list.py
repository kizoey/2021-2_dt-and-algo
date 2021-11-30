"""
queue_linked_list.py: create queue linked list, 큐 연결리스트 (연결된 큐)

- __init__: initialization of parameters (size, front, rear)
- enqueue: insert element into queue linked list (후단에서 데이터 추가)
- dequeue: delete top element from queue linked list (전단에서 데이터 삭제)
- queue_print: print total elements of queue linked list

- requirements: Node class (노드 생성)
"""


class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Queue_Linked:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    # 데이터 큐 연결리스트에 삽입
    def enqueue(self, item):
        self.new_node = Node(item, None)
        if self.size == 0:  # 빈 큐라면 front=rear=new_node
            self.front = self.new_node
            self.rear = self.new_node
        else:
            self.rear.next = self.new_node
            self.rear = self.new_node
        self.size += 1

    # 데이터 큐 연결리스트에서 삭제
    def dequeue(self):
        if self.size is not None:
            delete_item = self.front.item
            self.front = self.front.next
            self.size -= 1
        else:
            self.rear = None
        return delete_item

    # 현재 큐에 들어있는 데이터 원소 확인
    def queue_print(self):
        p = self.front
        print('Front: ', end=' ')
        while p:
            if p.next != None:  # front 뒤에도 계속해서 데이터가 있다면 print
                print(p.item, '->', end=' ')
            else:
                print(p.item, end=' ')
            p = p.next
        print(' :Rear')


if __name__ == '__main__':
    qul = Queue_Linked()
    qul.enqueue('my')  # [my]
    qul.enqueue('name')  # [my] - [name]
    qul.enqueue('is')  # [my] - [name] - [is]
    qul.queue_print()
    print(qul.dequeue())  # [name] - [is], my dequeued
    print(qul.dequeue())  # [is], name dequeued
    qul.queue_print()
