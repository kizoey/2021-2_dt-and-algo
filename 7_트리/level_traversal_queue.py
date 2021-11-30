"""
level_traversal_tree.py: level traversal using queue, 층별순회
층별 순회: 층별로 내려오면서 좌측 노드 -> 우측 노드로 순회하는 방법

- input: list of numbers (List)
- output: list of numbers (List)
"""

'''
[층별 순회]
Level_Order(TreeNode * root){
    queue q
    init(q)
    if not root: return
    while isEmpty is not True:
        p = dequeue(q)
        print(p)
        if (p -> left), enqueue(p -> left)
        if (p -> right), enqueue(p -> right)
        }
    }
'''

from collections import deque


def level_queue(self, num):
    queue = deque([num])
    while queue:
        t = queue.popleft()
        if t.item is not None:
            print(str(t.item), '', end=' ')
        if t.left is not None:
            queue.append(t.left)
        if t.right is not None:
            queue.append(t.right)
