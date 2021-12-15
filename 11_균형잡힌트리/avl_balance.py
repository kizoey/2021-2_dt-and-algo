"""
avl_balance: AVL 트리의 균형도 계산 (모두 0, 1, -1이 되도록 유지)
"""


class Node(object):
  def __init__(self, key, height, left=None,right=None):
    self.key = key
    self.height = height
    self.left = left
    self.right = right


class AVL(object):
  def __init__(self):
    self.root = None

  def balance(self,node):
    if self.bf(node) > 1: # LL 경우
      if self.bf(node.left) < 0: # LR 경우
        node.left = self.rotate_left(node.left) # LL 로 만듬
      node = self.rotate_right(node)
    elif self.bf(node) < -1: # RR 경우
      if self.bf(node.right) > 0: # RL 경우
        node.right = self.rotate_right(node.right)
      node = self.rotate_left(node)
    return node

  def bf(self,node):
    return self.height(node.left) - self.height(node.right)