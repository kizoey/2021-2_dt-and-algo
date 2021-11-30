"""
recursive_fibonacci.py: return fibonacci series, 단일 피보나치 수열

- input: number (int)
- output: number (int)
"""


# 재귀함수 사용 (피보나치 수열 결과만 반환)
def fibonacci_result(num):
    if num < 0:
        return print(f'Range out of number(negative).')
    elif 0 <= num <= 1:  # 0~1 사이인 경우 피보나치 수열의 결과는 자기 자신임
        return num
    else:
        return fibonacci_result(num-1) + fibonacci_result(num-2)


# 반복문 사용 (피보나치 수열 결과와 과정 반환)
def fibonacci_loop_repeat(num):
    f1, f2 = 1, -1
    result = []  # 피보나치 수열을 담는 리스트
    for i in range(num):
        tmp = f1
        f1 += f2
        f2 = tmp
        result.append(f1)
    return result


# 재귀함수 사용 (피보나치 수열 결과와 과정 반환)
def fibonacci_loop_recursive(num):
    if num < 0:
        return print(f'Range out of number(negative).')
    elif 1 <= num <= 2:
        return 1
    else:
        output = fibonacci_loop_recursive(num-1) + fibonacci_loop_recursive(num-2)
        return output


if __name__ == '__main__':
    fibonacci_n = int(input('Enter Fibonacci number: '))
    result = []
    for i in range(1, fibonacci_n+1):
        result.append(fibonacci_loop_recursive(i))
    print(f'{fibonacci_n}개의 피보나치 수열: {result}')
