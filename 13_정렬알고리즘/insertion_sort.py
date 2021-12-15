"""
insertion_sort: 삽입 정렬
"""

def insertion(data):
  for i in range(1,len(data)):
    for j in range(i,0,-1):
      if data[j-1] > data[j]:
        data[j],data[j-1] = data[j-1],data[j]