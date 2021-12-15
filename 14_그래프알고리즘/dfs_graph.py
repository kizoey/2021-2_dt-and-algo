"""
dfs_graph: 특정 정점부터 출발해 DFS를 적용한 그래프 알고리즘
"""

# 정점 3부터 출발해서 DFS를 적용한 그래프 알고리즘
def dfs_s(data,T):
  tovisit = [T]
  visited = []
  while tovisit:
    n = tovisit.pop()
    if n not in visited:
      visited.append(n)
      for j in reversed(data[n]):
        tovisit.append(j)
  return visited


if __name__ == "__main__":
  data = [[1],[0,2,3],[1,4],[1,4,5],[2,3],[3,6,7],[5,7],[5,8,9],[7,9],[7]]
  T = 3
  print(dfs_s(data,T))