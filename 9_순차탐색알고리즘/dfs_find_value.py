"""
dfs_find_value: DFS로 특정 값 검색
"""

# 특정 값인 5를 검색, 시작 노드=1
def dfs_f(data, start_n, search_n):
  dfs_v[start_n] = True
  if start_n == search_n:
    print(f'{search_n}을 찾음.')
    return
  for i in data[start_n]:
    if not dfs_v[i]:  # 방문완료되지 않았으면
        dfs_f(data,i,search_n)


#  인접리스트로 그래프 구현
if __name__ == "__main__":
  data = [[],
  [2,3,8],  # 1번노드의 인접노드,
  [1,7],  # 2번노드의 인접노드
  [1,4,5],  # 3번노드의 인접노드
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7],]
  dfs_v = [False]*len(data)  # 방문노드 표시
  dfs_f(data, 1, 5)
