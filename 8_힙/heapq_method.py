"""
heapq_method: heapq 모듈 활용
: min heap만 구현 가능한 모듈이므로 max heap 구현시 -1 곱해서 사용
"""
import heapq

def heapq_module(value):
  data = []
  result = []
  for s1 in value:
    heapq.heappush(data, -s1)
  while len(data) > 0:
    a = heapq.heappop(data)
    result.append(-a)
  return result


if __name__ == "__main__":
  value = [90,50,80,30,100,80,60,20,10,110,40]
  result = heapq