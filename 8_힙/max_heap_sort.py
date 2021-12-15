"""
max_heap_sort: 최대 힙 정렬
"""


class MaxBHeap:
  def __init__(self,bt):
    self.bt = bt
    self.N = len(bt)-1


  def delete_bh(self):
    if len(self.bt) == 1:
      print("Tree Empty")
    elif len(self.bt) == 2:
      # self.bt.pop(-1)
      return self.bt.pop()
    else:
      temp = self.bt[1]
      self.bt[1] = self.bt[self.N]
      self.bt.pop(-1)  # self.bt.pop(self.N)
      self.N -= 1
      self.down_heap(1)
      return temp


  def sort_heap(self):
    sort_max = []
    while len(self.bt) > 1:
      sort_max.append(self.delete_bh())
    return sort_max