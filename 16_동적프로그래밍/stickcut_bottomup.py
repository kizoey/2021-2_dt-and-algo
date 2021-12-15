"""
stickcut_bottomup: 막대 자르기 (bottom-up 방식)
"""
# 반복문 사용
import sys


def cutRod(price, n):
  val = [0 for x in range(n+1)]
  val[0] = 0
  # 테이블 val[] 을 만들고 bottom up 방식을 이용함.
  # 테이블의 마지막 결과값을 반환함.
  for i in range(1, n+1):
    max_val = -sys.maxsize-1
    for j in range(i):
      # print(f'val:: {val}')
      max_val = max(max_val, price[j] + val[i-j-1])
    val[i] = max_val
  return val[n]