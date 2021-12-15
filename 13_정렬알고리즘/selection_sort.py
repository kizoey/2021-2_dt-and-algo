"""
selection_sort: 선택 정렬
"""
def selection(data):
  for j in range(len(data)-1):
    min_ = j
  for i in range(j+1,len(data)):
    if data[i] < data[min_]:
      min_ = i
  data[j], data[min_] = data[min_], data[j]


if __name__ == "__main__":
    data = [90,20,40,3,7,14,76,45,28,38,17,9]
    print(f'before sort: {data}')
    selection(data)
    print(f'after sort: {data}')