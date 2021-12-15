"""
radix_sort: 기수 정렬
"""
from collections import deque

def radixsort(data):
  max_length = len(str(max(data)))  # 최대 자릿수 확인을 위해 문자열로 변환
  data = list(map(lambda x: f'{x:0>{max_length}}', data))  # 최대 자릿수보다 작은 데이터에 0 을 붙이는 코드 (자릿수 맞추기)
  buckets = [deque() for _ in range(10)]  # 십진수이므로 10개의 bucket 생성
  for i in range(max_length):
    for d in data:
      bucket_n = int(d[max_length-i-1])  # 맨 끝자리의 수를 저장 123이면 3을 저장
      buckets[bucket_n].append(d)  # 3에 해당되는 버킷에 123을 저장
    collect(data, buckets)
    print(data)
  return list(map(int, data))


def collect(data,buckets):
  data.clear()
  for bucket in buckets:
    for _ in range(len(bucket)):
      data.append(bucket.popleft())


if __name__ == "__main__":
  data = [153, 897, 432, 910, 378, 878]  # 자릿수가 모두 같은 데이터에만 적용
  print(radixsort(data))