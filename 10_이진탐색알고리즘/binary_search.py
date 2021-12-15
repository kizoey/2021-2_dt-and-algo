"""
binary_search: 이진탐색 알고리즘
"""

binary_list = []

def binary_search(left, right, k):
  if left > right:
    return None
  middle = (left + right) // 2
  if binary_list[middle] == k:
    return middle
  if binary_list[middle] > k:
    binary_search(left, middle-1, k)  # 중간 인덱스의 앞부분 탐색
  else:
    binary_search(middle+1, right, k)  # 중간 인덱스의 뒷부분 탐색
