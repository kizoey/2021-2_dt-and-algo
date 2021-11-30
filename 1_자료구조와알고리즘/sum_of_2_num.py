"""
sum_of_2_num.py: brute-force approach-based, return index of 2 numbers added
- big-Oh: O(n^2)

- input: list of numbers (List)
- output: index of 2 numbers (List)
- purpose: find numbers that add up to be the target number, return the added numbers' indices
"""

from typing import *  # use typehint
import time


def twoSum(data: List[int], target: int) -> List[int]:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                return [i, j]


if __name__ == '__main__':
    start = time.time()
    data = [2, 3, 6, 8, 9, 4, 5, 123, 56, 43, 22]
    target = 28
    result = twoSum(data, target)
    end = time.time()

    print(f'Index of 2 numbers: {result}')
    print(f'Running time: {end-start}')