"""
prim: Prim 알고리즘으로 위상트리 탐색
"""

# heapq 이용해서 prim 알고리즘 적용
from collections import defaultdict
import heapq  # list를 이용하며, heapq는 min heap
# min heap(최소 힙): 항상 자식 노드가 부모 노드의 값보다 큼


def prim_tree(graph, starting_vertex):
  mst = defaultdict(set) #set 형 dict 생성, 존재하지않은 key가 주어지면 새로 생성
  visited = set([starting_vertex])
  edges = [
           (cost, starting_vertex, to)
           for to, cost in graph[starting_vertex].items() ]
  # print(f'edges:: {edges}') →edges:: [(4, '0', '1'), (3, '0', '2')]
  heapq.heapify(edges) #기존 리스트를 heap 으로 바꾸는 함수
  total=0
  while edges:
    cost, frm, to = heapq.heappop(edges)
    if to not in visited:
      visited.add(to)
      mst[frm].add(to)
      total += cost
      for to_next, cost in graph[to].items():
        if to_next not in visited:
          heapq.heappush(edges, (cost, to, to_next))
  print(f'total cost:: {total}')
  return mst