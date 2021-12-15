"""
create_bst: 이진탐색트리 생성
"""
class Node:
  def __init_(self, key, value, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right


class BST:
  def __init__(self):
    self.root = None

  def bst_create(self, key):
    self.root = self.bst_insert(self.root, key)

  def bst_insert(self, root, key):
    if root == None:
      return Node(key)
    if root.key > key:
      root.left = self.bst_insert(root.left, key)
    elif root.key < key:
      root.right = self.bst_insert(root.right, key)
    else:
      root.value = key
    return root


# 일반 이진탐색트리
if __name__ == '__main__':
  bst = BST()
  base = [i for i in map(int, input("Enter Numbers > ").split())]
  for i in range(len(base)):
    bst.bst_create(base[i])


# 실제 이진탐색트리
if __name__ == '__main__':
  bst = BST()
  data = [[50,'apple'], [60,'melon'], [20,'lime'], [10,'kiwi'],\
          [40,'peach'], [25,'orange'], [15,'grape'], [80,'lemon'],\
          [70,'cherry'], [5,'pear'], [35,'mango'], [45,'plum']]
for i in range(len(data)):
  bst.bst_create(data[i][0], data[i][1])