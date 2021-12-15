"""
search_bst: 이진탐색트리 탐색
"""
# 재귀함수 사용
def get(self, key):
  return self.get_value(self.root, k)

def get_value(self, r,k):
  if r == None:
    return None
  if r.key > k:
    return self.get_value(r.left,k)
  elif r.key < k:
    return self.get_value(r.right,k)
  else:
    return r.value

# 순환문 loop 사용
def get_value(self,r,k):
  if r==None:
    return None
  while r != None:
    if r.key == k:
      return r
    elif r.key>k:
      r = r.left
    else:
      r = r.right
  return None