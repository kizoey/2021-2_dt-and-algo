"""
binary_tree.py: Class of BinaryTree(), 이진 트리
이진 트리: 모든 노드가 최대 2개의 서브 트리를 갖고 있는 트리

- __init__: initialization of parameters (root)  root: 루트노드
- make_tree: make tree with left node right node

- requirements: Node class (노드 생성)
"""


# 연결리스트 구성요소인 노드 생성 클래스 (item=데이터/항목, left=왼쪽 자식, right=오른쪽 자식)
class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def make_tree(self, node, left, right):
        if self.root is None:
            self.root = node
        node.left = left
        node.right = right


# 완전 이진트리 생성 (루트 레벨 1이라는 가정 하,
if __name__ == '__main__':
    tree = BinaryTree()
    value = [100, 200, 300, 400, 500]
    n = []
    for i in value:
        n.append(Node(i))
    for i in range(len(n) // 2):
        if 2 * i + 1 <= len(value) - 1:  # 오른쪽 자식까지 만들 수 있을만큼 value가 있으면, 왼쪽부터 채우기
            tree.make_tree(n[i], n[2 * i], n[2 * i + 1])  # 왼쪽 자식 인덱스: 2*i, 오른쪽 자식 인덱스: 2*i+1
        else:
            tree.make_tree(n[i], n[2*i], None)

    # 왼쪽 자식 - 루트 노드 - 오른쪽 자식 순으로 출력
    for i in range(len(n) // 2):
        if 2 * i + 1 <= len(value) - 1:
            print(n[i].item, '-', n[2 * i].item, '-', n[2 * i + 1].item)  # 왼쪽 자식 인덱스: 2*i, 오른쪽 자식 인덱스: 2*i+1
        else:
            print(n[i].item, '-', n[2 * i].item, '-', None)
