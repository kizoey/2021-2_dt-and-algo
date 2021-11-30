"""
preorder_traversal.py: preorder traversal, 전위순회
전위 순회: 루트를 먼저 방문하는 순회방법

- __init__: initialization of parameters (root)  root: 루트노드
- preorder: 전위순회 알고리즘
- height: return maximum height between left and right

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

    # 전위순회 알고리즘
    def preorder(self, num):
        if num.item is not None:
            print(str(num.item), '', end=' ')
            if num.left:
                self.preorder(num.left)
            if num.right:
                self.preorder(num.right)

    # print higher height between left child, right child
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1


'''
[전위순회]
preorder(TreeNode * root)}
    if root{
        print(root)
        preorder(root -> left)  왼쪽 서브트리 방문
        preorder(root -> right) 오른쪽 서브트리 방문
    }
}
'''
if __name__ == '__main__':
    tree = BinaryTree()
    value = ['A', 'B', 'C', 'D', 'E', None, 'F', 'G', 'H', None, None, None, None, 'I', None]

    n = []
    for i in value:
        n.append(Node(i))
    for i in range(len(value) // 2):
        if i == 0:
            n[i].left = n[i + 1]
            n[i].right = n[i + 2]
        else:
            n[i].left = n[2 * i + 1]
            if 2 * i + 2 <= len(value) - 1:
                n[i].right = n[2 * i + 2]

    tree.root = n[0]
    print('트리 높이:', tree.height(tree.root))
    print('전위순회:', end='')
    tree.preorder(tree.root)
