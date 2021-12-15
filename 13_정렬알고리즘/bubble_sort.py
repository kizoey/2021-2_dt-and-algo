"""
bubble_sort: 버블 정렬
"""

def bubble(data):
  for i in range(len(data)):
    for j in range(1,len(data)-i):
      if data[j] < data[j-1]:
        data[j],data[j-1] = data[j-1],data[j]