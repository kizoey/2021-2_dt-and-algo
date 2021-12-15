"""
binary_tree_delete: 이진탐색트리의 삭제코드, 삭제가 된 이진탐색트리의 노드값은 inorder (중위순회) 이용해서 출력
"""


class Bst(object):
    def __init__(self):
        self.root = None

    # None 출력하지 않는 중위순회 함수
    def inorder_traversal(self, t):
        if t.item is not None:
            if t.left:  # 왼쪽에 방문하면, 왼쪽 서브트리 순차적으로 방문하고 출력
                self.inorder_traversal(t.left)
            print(str(t.item), ' ', end='')
            if t.right:  # 오른쪽 방문
                self.inorder_traversal(t.right)

    def bst_remove(self, key):
        self.root, remove = self.remove_f(self.root, key)
        remove.left = remove.right = None
        return self.inorder_traversal(remove)

    def remove_f(self, t, key):
        # 삭제대상 노드의 자식개수의 종류에 따른 삭제방법 코드 작성
        if key == t.data:
            r_node = True
            # 자식이 둘 다 있는 경우
            if t.left and t.right:
                parent, child = t, t.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = t.left
                if parent != t:
                    parent.left = child.right
                    child.right = t.right
                t = child
            # 자식이 하나만 있는 경우
            elif t.left or t.right:
                t = t.left or t.right
            # 자식이 없는 경우
            else:
                t = None
        elif key > t.key:
            t.right, r_node = self.remove_f(t.right, key)
        elif key < t.key:
            t.left, r_node = self.remove_f(t.left, key)
        else:
            return None, None
        return t, r_node
