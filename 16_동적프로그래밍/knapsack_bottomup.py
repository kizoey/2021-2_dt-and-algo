"""
knapsack_bottomup: 배낭 문제 (bottom-up 방식)
   - limit_w: 배낭의 한도, wt: 각 보석의 무게, val:보석의 가치
   - n: 보석 수
"""
import sys


def fractional_kanpsack(limit_w, wt,val, n):
  # 공간이 없음을 나타내기 위해 0번 index를 추가 생성함
  tablet = [[0 for i in range(limit_w+1)] for j in range(n+1)]
  val = [0]+val
  wt = [0]+wt
  for i in range(1,n+1):
    for j in range(1,limit_w+1):
      if wt[i] <= j:
        tablet[i][j] = max(val[i]+tablet[i-1][j-wt[i]], tablet[i-1][j])
      else:
        tablet[i][j] = tablet[i-1][j]
  for i in range(n+1):
    print(f'{tablet[i]}')
  return tablet[n][limit_w]


if __name__ == "__main__":
  n = 3
  limit_w = 4. # n,limit_w = map(int, sys.stdin.readline().strip().split())
  wt = [1,3,4]
  val = [3,4,5]
  print(fractional_kanpsack(limit_w, wt, val, n))