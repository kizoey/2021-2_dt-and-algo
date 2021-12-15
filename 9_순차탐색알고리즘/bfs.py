"""
bfs: Breath-first search (너비우선탐색)
: 큐(queue) 자료구조 사용하기 위해서 deque 라이브러리 사용
"""
from collections import deque

def bfs_f(data,start):
  queue = deque([start])
  bfs_visited[start] = True
  while queue:
    n = queue.popleft()
    print(n, end= '->')
    for i in data[n]:
      if not bfs_visited[i]:
        queue.append(i) 
        bfs_visited[i] = True


if __name__ == "__main__":
  data = [[],
          [2,3,8],  # 1번 노드의 인접노드
          [1,7],  # 2번 노드의 인접노드
          [1,4,5],  # 3번 노드의 인접노드
          [3,5],
          [3,4],
          [7],
          [2,6,8],
          [1,7],]
bfs_visited = [False]*len(data)
bfs_f(data, 1)