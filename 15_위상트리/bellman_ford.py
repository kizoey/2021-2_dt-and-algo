"""
bellman_ford: Bellman-Ford 알고리즘으로 위상트리 탐색
"""

def bellman_ford(G, s):
  edges, predecessor = dict(), dict()  # 간선, 각 노드의 이전 노드를 저장
  # 1단계, 초기화
  for i in G:
    edges[i], predecessor[i] = float('inf'), None
  edges[s] = 0
  # 2-3단계, V-1 만큼 반복
  for _ in range(len(G)-1):
    for i in G:  # 그래프의 노드
      for j in G[i]:  # 각 노드마다 모든 인접 노드 탐색
        if edges[j] > edges[i] + G[i][j]:
          edges[j] = edges[i] + G[i][j]
          predecessor[j] = i  # 노드 추가
  # negative cycle 검사, 수정할 간선 가중치 존재 확인
  for i in G:
    for j in G[i]:
      if edges[j] > edges[i] + G[i][j]:
        return False, 'negative cycle'
  return edges, predecessor


if __name__ == "__main__":
  G = {'0': {'1':4,'2':5},'1':{'2':-2},'2':{'3':3},
       '3':{'4':4,'5':-1},'4':{'5':4}, '5':{'3':3}}
  print(bellman_ford(G,'0'))