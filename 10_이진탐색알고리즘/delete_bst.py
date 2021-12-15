"""
delete_bst: 이진탐색트리 삭제
 = 1번째 case: 삭제 노드가 단말 노드인 경우
 - 2번째 case: 삭제 노드의 자식이 하나, 오른쪽/왼쪽 하나인 경우
 - 3번째 case: 삭제 노드의 자식이 왼쪽과 오른쪽에 모두 있는 경우
"""
def inorder(self,t):
  if t :
    self.inorder(t.left)
    print(f'{t.key} ', end='' )
    self.inorder(t.right)


def remove_f(self, t, key):
  if t is None:
    return None, None
  elif key > t.key:
    t.right, r_node = self.remove_f(t.right, key)
  elif key < t.key:
    t.left, r_node = self.remove_f(t.left,key)
  else:
    # 삭제노드가 leaf 노드인 경우
    if not t.left and not t.right:
      r_node = t
      t = None
    # 삭제노드의 자식이 하나, 오른쪽 또는 왼쪽 자식만 존재
    elif not t.left:
      r_node = t
      t = t.right
    elif not t.right:
      r_node = t
      t = t.left
    else: # 삭제노드가 왼쪽과 오른쪽 자식이 모두 존재하는 경우
      another = t.left
      print(f'another: {another.key}')
      while another.right:
        another = another.right
      t.key, another.key = another.key, t.key
      print(f't.key, another.key:: {t.key} & {another.key}')
      t.left, r_node = self.remove_f(t.left, another.key)
  return t, r_node