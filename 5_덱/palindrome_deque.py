"""
palindrome_deque.py: check whether it is palindrome, using deque, 덱 활용

- input: string sequence (str)
- output: palindrome or not (bool)
- purpose: find whether the input sequence of numbers are palindrome by using DT deque
"""

from collections import deque


def palindrome_deque(data: str) -> bool:
    string_lst = deque()
    for char in data:
        if char.isalpha():
            string_lst.append(char.lower())
    while len(string_lst) > 1:
        if string_lst.popleft() != string_lst.pop():  # 전단의 요소 != 후단의 요소면 False
            return False
    return True


if __name__ == '__main__':
    data = input('Input sequence:')
    print(f'Is it Palindrome?', palindrome_deque(data))