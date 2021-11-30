"""
postorder_traversal.py: postorder traversal, 후위순회
후위 순회: 루트를 가장 나중에 방문하는 순회방법, 왼쪽 자식에서 오른쪽 자식으로 방문

- __init__: initialization of parameters (root)  root: 루트노드
- postorder: 후위순회 알고리즘

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

    # 중위순회 알고리즘, None 출력하지 않는 경우
    def postorder(self, num):
        if num.item is not None:
            if num.left:
                self.postorder(num.left)
            if num.right:
                self.postorder(num.right)
            print(str(num.item), '', end=' ')


'''
[후위순회]
postorder(TreeNode * root)}
    if root{
        postorder(root -> left)  왼쪽 서브트리 방문
        postorder(root -> right) 오른쪽 서브트리 방문
        print(root)
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
    print('후위순회:', end='')
    tree.postorder(tree.root)
