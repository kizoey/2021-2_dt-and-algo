"""
quick_sort: 퀵 정렬
"""
import random

def rand_shuffle(data):  # Knuth의 random shuffle
  # 정렬된 리스트의 경우 시간 소요가 더 오래 걸리기 때문에 random shuffling 진행
  N = len(data)
  for i in range(N):
    temp = random.randint(0,i)
    data[i], data[temp] = data[temp], data[i]


def quicksort(data):
  N = len(data)
  if N < 1:
    return data
  else:
    pivot = data[N-1]
    less = [i for i in data[:N-1] if i <= pivot]
    greater = [i for i in data[:N-1] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    data = [50,3,8,11,45,70,37,20,8,29,77,65,33]
    rand_shuffle(data)
    print(data)
    print(quicksort(data))
