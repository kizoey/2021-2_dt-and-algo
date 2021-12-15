"""
dfs_find_cc: DFS로 연결 요소(connected components) 찾기
: 방향이 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램
"""
import sys

def dfs():
  while stack:
    x = stack.pop()
  for each in adj[x]:
    if visited[each] == 0:
      visited[each] = 1
      stack.append(each)


# V: vertex, E: edge
V, E = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
stack = []

# 모든 edge를 리스트에 저장
for _ in range(1,E+1):
  x, y = map(int,sys.stdin.readline().split(" "))
  adj[x].append(y)
  adj[y].append(x)
print(adj)

# 모든 vertex 확인
count = 0
for i in range(1,V+1):
  if visited[i] == 0:
    count += 1
    stack.append(i)
    dfs()
print(count)