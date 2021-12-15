"""
prime_algorithm.py: Minimum spanning tree (신장트리) 비용 최소화하는 prime 알고리즘 구현
- import heapq 사용
"""

from collections import defaultdict
from heapq import *


def prim(start_node, edges):
    mst = list()
    # 모든 간선의 정보를 adjacent_egdes에 저장
    adjacent_egdes = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_egdes[n1].append((weight, n1, n2))
        adjacent_egdes[n2].append((weight, n2, n1))

    # 연결된 노드 집합에 시작 노드 포함
    connected_nodes = set(start_node)

    # 시작(특정) 노드에 연결된 간선 리스트
    candidate_edge_list = adjacent_egdes[start_node]
    heapify(candidate_edge_list)  # 가중치 순으로 간선 리스트 정렬

    # 최소 가중치를 가지는 간선부터 추출
    while candidate_edge_list:
        # 최소 가중치 간선이 추출됨
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
            # n2의 간선들 중
            # 연결된 노드 집합에 없는 노드의 간선들만
            # 후보 간선 리스트에 추가함
            for edge in adjacent_egdes[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst


if __name__ == "__main__":
    myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
    ]
    print(prim('A', myedges))