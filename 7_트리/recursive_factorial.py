"""
recursive_factorial.py: return cumulative factorial up to certain number, 누적 계승 구하기
- 반복문 사용
- 재귀함수 사용

- input: number (int)
- output: number (int)
"""

import math


# 반복문 사용
def factorial_repeat(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


# 재귀함수 사용
def factorial_recursive(num):
    if num < 0 and num != int(num):
        return print('Wrong Input.')
    elif num == 0 or num == 1:  # 0!, 1! = 1
        return 1
    else:
        return num * factorial_recursive(num-1)


if __name__ == '__main__':
    value = int(input('Enter Value:'))
    result = factorial_recursive(value)
    print(f'Factorial up to {value} is {result}')
