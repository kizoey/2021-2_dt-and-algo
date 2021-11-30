"""
stock_maximum_profit.py: finding the maximum profit of stock prices, 주식의 최대 이윤

- input: sequence of stock prices (List)
- output: maximum profit (int)
- purpose: find the maximum profit of selling at highest price, buying at lowest price,
           but also consider the consequence of prices (no going backward direction)
"""

from typing import List
import sys  # sys: maxsize, 정수의 최댓값은 원래는 무한대이지만 파이썬 상에서는 특정한 정수 최댓값을 지정함 (sys.maxsize 출력 가능)
# sys.maxsize, 최대 정수값 = 9223372036854775807
# sys.maxsize, 최소 정수값 = -9223372036854775807


def stock_profit(prices: List[int]) -> int:
    max_profit = 0  # 이윤 없는 경우 0 반환
    min_price = sys.maxsize  # 엄청 큰 값을 설정
    for var in prices:
        min_price = min(min_price, var)
        max_profit = max(max_profit, var-min_price)
    return max_profit


if __name__ == '__main__':
    prices = [7, 5, 6, 4, 10, 8, 9, 16]
    print(f'Maximum profit: {stock_profit(prices)}')  # 12: 16-4
