"""
ddeok_cut: 가래떡을 원하는 길이의 합이 되도록 자르는 프로그램 (이진탐색활용)
- 가래떡을 판매할 때, 주어진 가래떡들을 정해진 높이의 절단기를 통해 절단
- 절단된 가래떡의 합이 손님이 원하는 가래떡의 길이가 되도록 절단기의 최적 높이를 설정하는 문제
예) 가래떡의 길이가 19, 14, 10, 17 로 주어진 경우
• 손님이 4 개의 가래떡을 자른 합의 결과인 6을 원할 때
• 절단기를 15로 맞춰 자르면 4, 0, 0, 2 가 되어 손님이 원하는 6을 맞출 수 있음
• 이 경우의 결과값은 15가 됨
• 즉 손님이 요청한 총 길이가 M일 때 적어도 M 만큼의 가래떡을 얻기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 문제임
"""

# 입력값, 떡의 개수 n, 손님이 요청한 떡의 길이 m
# 주어진 떡의 개수 별 길이 rice_len
n, m = list(map(int, input().split()))
rice_len = list(map(int, input().split()))

start = 0
end = max(rice_len)

# 이진 탐색 활용
result = 0
while start <= end:
    total = 0
    middle = (start+end) // 2
    for r in rice_len:
        if r > middle:
            total += r - middle
    # 떡의 양이 부족한 경우에는 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = middle - 1
    # 떡의 양이 충분한 경우에는 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = middle
        start = middle + 1

print(result)
