"""
llrb_insert: LLRB 트리의 삽입
"""
def insert(self, key,value):
  if self.root is None:
    self.root = LeftRB.Node(key,value)
    self.root = LeftRB.Node.insert(self.root, key,value)
    self.root.color = BLACK


from leftrb.llrb import *

items = [(10,'apple'),(20,'lime'),(30,'mango'),(40,'pear'),(50,'straw'),
          (5,'banana'),(15,'melon'),(60,'apple'),(70,'peach'),(80,'persimmon'),
          (25,'grape'),]
rb = LeftRB()

for key,value in items:
  rb.insert(key,value)
  rb.inorder(rb.root)