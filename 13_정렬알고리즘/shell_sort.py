"""
shell_sort: 쉘 정렬
"""
import math

def shell(data):
  size = len(data)
  gap = size//2
  if gap%2 == 0:
    gap += 1
  while gap >=1:
    for i in range(gap, size):
      for j in range(gap):
        shell_insert(data,j,size, gap)
    gap //=2


def shell_insert(data,start,size, gap):
  for i in range(start+gap,size, gap):
    key = data[i]
    j = i-gap
    while j >= start and data[j] > key:
      data[j+gap], data[j] = data[j],key
      j -= gap