"""
stickcut_topdown: 막대 자르기 (top-down 방식)
"""
# 재귀함수 사용
import sys
cut_dict ={}  # memoization


def cutRod(price, n):
  if(n <= 0):
    return 0
  max_val = -sys.maxsize-1
  if n in cut_dict:
    return cut_dict[n]
  for i in range(0, n):
    max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    cut_dict[n] = max_val
  return max_val