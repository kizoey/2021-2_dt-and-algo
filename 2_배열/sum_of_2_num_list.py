"""
sum_of_2_num_list.py: difference of target and list based, return index of 2 numbers added
- big-Oh: O(n)

- input: list of numbers (List)
- output: index of 2 numbers (List)
- purpose: find numbers that add up to be the target number, return the added numbers' indices
"""

from typing import *  # use typehint
import time


def twoSum_list(data: List[int], target: int) -> List[int]:
    var_key = {}
    for i, var in enumerate(data):
        var_key[var] = i  # 딕셔너리에 추가(index as key, var as value)
        if target - var in var_key:  # target - num1 = num2 (num1+num2=target 원리 이용)
            return [var_key[target-var], i]


if __name__ == '__main__':
    start = time.time()
    data = [2, 3, 6, 8, 9, 4, 5, 123, 56, 43, 22]
    target = 28
    result = twoSum_list(data, target)
    end = time.time()

    print(f'Index of 2 numbers: {result}')
    print(f'Running time: {end-start}')