"""
product_wtout_self.py: finding the list of product without itself in the multiplication, 자신을 제외한 값들의 곱
- big-Oh: O(n)

- input: list of numbers (List)
- output: product of values (List)
- constraint: 모든 값들을 다 곱한 뒤 자기자신으로 나눠주는 단순한 연산 사용 불가
"""

from typing import List


def product_wtout_self(values: List[int]) -> List[int]:
    result = []
    # 왼쪽 값들의 곱 (n번, O(n))
    point = 1
    for i in range(len(values)):
        result.append(point)
        point *= values[i]  # 자신을 도달하기 전까지 곱하기

    # 오른쪽 값들의 곱 (n번, O(n))
    point = 1
    for i in range(len(values)-1, -1, -1):
        result[i] *= point
        point *= values[i]
    return result


if __name__ == '__main__':
    values = [1, 2, 3, 4]
    print(f'Product without itself: {product_wtout_self(values)}')
