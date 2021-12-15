"""
customize_merge_sort: 합병 정렬의 간단한 버전
"""

def merge(data,temp,left,mid,right):
  i = left
  j = mid+1
  for n in range(left, right+1):
    if i > mid:
      temp[n] = data[j]
      j += 1
    elif j > right:
      temp[n] = data[i]
      i += 1
    elif data[j] < data[i]:
      temp[n] = data[j]
      j += 1
    else:
      temp[n] = data[i]
      i += 1
  for n in range(left, right+1):
    data[n] = temp[n]