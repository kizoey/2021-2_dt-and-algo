"""
max_heap: 최대 힙의 메서드
- create_bheap: 최대 힙 생성
- insert_bheap: 삽입
- delete_bheap: 삭제
- down_heap: 최대 힙 아래로 탐색
- up_heap: 최대 힙 위로 탐색
- print_bheap: 출력
"""


class MaxBHeap:
    def __init__(self, bt):
        self.bt = bt
        self.N = len(bt) - 1

    # 무작위 데이터를 최대 힙으로 구성
    # 전체 데이터의 중간위치의 자식들 대소 비교
    def create_bheap(self):
        for i in range(self.N // 2, 0, -1):
            self.down_heap(i)  # 5,4,3,2,1대입

    def insert_bh(self, item):
        self.bt.append(item)
        self.N += 1
        self.up_heap(self.N)

    def delete_bh(self):
        if len(self.bt) == 1:
            print("Tree Empty")
        elif len(self.bt) == 2:
            self.bt.pop(-1)
        else:
            self.bt[1] = self.bt[self.N]
            self.bt.pop(-1)  # self.bt.pop(self.N)
            self.N -= 1
            self.down_heap(1)

    def down_heap(self, i):
        while 2 * i <= self.N:
            j = 2 * i
            if j < self.N and self.bt[j] < self.bt[j + 1]:
                j = j + 1
            if self.bt[i] > self.bt[j]:
                break
            self.bt[i], self.bt[j] = self.bt[j], self.bt[i]
            i = j

    def up_heap(self, i):
        while i > 1:
            if self.bt[i] > self.bt[i // 2]:
                self.bt[i], self.bt[i // 2] = self.bt[i // 2], self.bt[i]
            i = i // 2

    def print_bheap(self):
        for i in range(1, self.N + 1):
            print(f'{self.bt[i]:5d}', end='')
        print('\nSize of Heap : ', self.N)


if __name__ == '__main__':
    value = [None, 90, 50, 80, 30, 100, 80, 60, 20, 10, 110, 40]
    bh = MaxBHeap(bt)
    print('Before Max binary Heap')
    bh.print_bheap()
    bh.create_bheap()
    bh.print_bheap()
    print()
    bh.insert_bh(120)
    bh.print_bheap()
    bh.delete_bh()
    print()
    bh.print_bheap()