"""
dfs: Depth-first search (깊이우선탐색)
1. 스택 사용
   - 현재 노드와 인접한 노드 중 방문하지 않은 모든 노드를 스택에 입력
   - 현재 노드에 방문 표시 후 가장 최근에 입력된 노드 삭제
   - 1번째 단계 반복
   - 스택이 비면 탐색 종료
2. 재귀함수 사용
   - 최대 재귀깊이 1000으로 제한
   - 재귀깊이 확장하는 설정 가능 (import sys, sys.setrecursionlimit(1500))
"""


class Node:
  def __init__(self, item, left=None, right=None):
    self.item = item  # value of Node
    self.left = left  # left child of Node
    self.right = right  # right child of Node


# 스택 사용
def DFS_stack(T):
  '''
  스택구조를 이용한 깊이탐색 코드
  '''
  tovisit = [T]
  visited = []
  while tovisit:
    n = tovisit.pop()
    if n.item != None:
      visited.append(n.item)
    if n.right != None:
      tovisit.append(n.right)
    if n.left != None:
      tovisit.append(n.left)
  return visited


# 재귀호출 사용
def dfs_recursive(T):
  '''
  재귀호출을 이용한 깊이탐색 코드
  트리 구조에서 탐색은 travelsal 개념과 동일하므로, 깊이탐색은 전위, 중위, 후위 중에 하나를 선택
  '''
  if T is None:
    return
  print(f'{T.item} -> ', end=' ')
  dfs_recursive(T.left)
  dfs_recursive(T.right)


if __name__ == "__main__":
  T = Node(1,Node(3,Node(4,None,None),Node(5,None,None)), \
           Node(2, None, Node(7, Node(8,None,None), \
                              Node(6,None,None))))
  print(DFS_stack(T))