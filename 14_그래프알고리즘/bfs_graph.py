"""
bfs_graph: 특정 정점부터 출발해 BFS를 적용한 그래프 알고리즘
"""
from collections import deque

# 정점 3부터 출발해서 BFS를 적용한 그래프 알고리즘
def bfs_s(data,T):
  queue = deque([T])
  visited = [False for _ in range(len(data))]
  visited[T] = True
  while queue:
    n = queue.popleft()
    print(n, end=' ')
    for i in data[n]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


if __name__ == "__main__":
  data = [[1],[0,2,3],[1,4],[1,4,5],[2,3],
          [3,6,7],[5,7],[5,8,9],[7,9],[7]]
  T = 3
  bfs_s(data,T)