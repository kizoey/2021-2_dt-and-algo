"""
inorder_traversal.py: inorder traversal, 중위순회
중위 순회: 왼쪽 자식 방문한 뒤 루트 노드, 오른쪽 자식 방문

- __init__: initialization of parameters (root)  root: 루트노드
- inorder: 중위순회 알고리즘

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
    def inorder_1(self, num):
        if num.item is not None:
            if num.left:  # 왼쪽에 방문하면, 왼쪽 서브트리 순차적으로 방문하고 출력
                self.inorder_1(num.left)
            print(str(num.item), ' ', end='')
            if num.right:  # 오른쪽 방문
                self.inorder_1(num.right)

    # 중위순회 알고리즘, None 함께 출력하는 경우
    def inorder_2(self,num):
        if num is not None:
            self.inorder_1(num.left)
            print(f'{num.item}', end='' )
            self.inorder_1(num.right)


'''
[중위순회]
inorder(TreeNode * root)}
    if root{
        inorder(root -> left)  왼쪽 서브트리 방문
        print(root)
        inorder(root -> right) 오른쪽 서브트리 방문
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
    print('중위순회:', end='')
    tree.inorder_1(tree.root)
