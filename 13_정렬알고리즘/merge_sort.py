"""
merge_sort: 합병 정렬
"""

# 정렬데이터 나누기
def merge(left,right):
  if not left or not right:
    return left or right
  result = []
  i,j = 0,0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  if left[i:]:
    result.extend(left[i:])
  if right[j:]:
    result.extend(right[j:])
  return result

# 정렬데이터 합치기
def merge_divide(data):
  if len(data) <2 :
    return data
  mid = len(data)//2
  left = merge_divide(data[:mid])
  right = merge_divide(data[mid:])
  return merge(left, right)


if __name__ == "__main__":
  data = [10,7,36,8,19,9,33,56,15,12,32,2,6,45,69]
  print(merge_divide(data))