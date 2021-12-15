"""
mergeKLists: 우선순위 큐를 사용해서 K 개의 정렬된 리스트를 1 개의 정렬된 리스트로 병합
"""

from typing import List
from typing import Optional
from heapq import heappush, heappop, heapreplace, heapify


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next:
                heappop(heap)
            else:
                heapreplace(heap, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next
        return dummy.next


if __name__ == "__main__":
    data = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for i in range(len(data)):
        root = head = ListNode(data[i][0])
        for j in range(1, len(data[i])):
            new = ListNode(data[i][j])
            head.next = new
            head = new
        lists.append(root)
    print(lists)

    merge1 = Solution()
    result = merge1.mergeKLists(lists)
    while result:
        print(f'{result.val} --> ', end='')
        result = result.next
