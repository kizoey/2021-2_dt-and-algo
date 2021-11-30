"""
recursive_cumulative_sum.py: return cumulative sum up to certain number, 누적합 구하기
- 반복문 사용
- 재귀함수(어떤 함수가 종료되지 않은 상황에서 자신을 다시 호출하는 것) 사용

- input: number (int)
- output: number (int)
"""


# 반복문 사용
def cumulative_repeat(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum


# 재귀함수 사용
def cumulative_recursive(num):
    if num == 0:
        return 0
    else:
        return num + cumulative_recursive(num-1)


if __name__ == '__main__':
    value = int(input('Enter Value:'))
    result = cumulative_recursive(value)
    print(f'Cumulative sum up to {value} is {result}')
