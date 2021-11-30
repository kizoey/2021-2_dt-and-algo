"""
sum_2_num_by_position.py: sum 2 numbers by their position in each number, 자릿수별 두 수의 덧셈
- 역순으로 저장된 연결리스트의 숫자를 더하는 문제

- input: two numbers (Linked list), 2->4->3, 5->6->4
- output: number (int)

- requirements: Node class (노드 생성)
"""


class Node:
    def __init__(self,item):
        self.item = item
        self.next = None


'''
[linked_list_sum]
- 입력값 2개와 자리올림수를 합한 결과를 다음 자리 올림수에서 사용
- 합산결과의 몫과 나머지 중 나머지 = 연산결과, 몫 = 다음 자리올림수
'''


def linked_list_sum(first, second):
    root = head = Node(0)
    carry = 0  # 올림하는 경우 보관하는 곳
    while first or second or carry:
        sum = 0
        if first:
            sum += first.item
            first = first.next
        if second:
            sum += second.item
            second = second.next

        carry, val = divmod(sum+carry, 10)  # divmod: 몫/나머지 반환
        head.next = Node(val)
        head = head.next
    return root.next


'''
[역순으로 저장된 연결리스트의 숫자 더하기]
step 1. 입력 숫자의 각 자리별로 더한다.
step 2. 올림의 경우, 0만 남기고 1은 올린다. (10으로 나눠서 몫이 있으면 그대로 올리고, 나머지가 있으면 나머지만 사용)
'''
if __name__ == '__main__':
    f1 = Node(2); s1 = Node(5)
    f2 = Node(4); s2 = Node(6)
    f3 = Node(3); s3 = Node(4)
    f1.next = f2; s1.next = s2
    f2.next = f3; s2.next = s3

    result = linked_list_sum(f1, s1)
    while result:
        print(f'{result.item} -> ', end=' ')
        result = result.next
