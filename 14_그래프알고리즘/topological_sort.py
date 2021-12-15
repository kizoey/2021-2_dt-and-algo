"""
topological_sort: 위상 정렬
   - 역방향으로 코드 구현
"""

def dfs(v):
  visited[v] = True
  for i in prerequisite[v]:
    if not visited[i]:
      dfs(i)
  ts.append(v)


if __name__ == "__main__":
    prerequisite = [[2],[2],[4],[2,4,5],[7],[4,6],[7],[]]
    dic = {0:'응용',1:'미적',2:'선형',3:'컴언어',4:'ORI',5:'자료',6:'객체지향',7:'ORII',}
    N = len(prerequisite)
    visited = [False]*N
    ts = []
    for i in range(N):
      if not visited[i]:
        dfs(i)
    ts.reverse()

    for i in range(N):
      print(f'{dic[ts[i]]} ', end = ' ')
    print()