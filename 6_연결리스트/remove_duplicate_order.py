"""
remove_duplicate_order.py: remove duplicate string in list and order by alphabetical order, 중복문자 제거 후 사전식 순서로 나열
- 중복없이 사용: collections 패키지의 Count 사용해서 문자열과 각 문자열의 개수 출력
- 중복되는 경우, 원자리 그대로 유지하고 나머지만 알파벳 순서대로 나열
- 최종적인 답안은 문자열 리스트에서 join 함수로 서로의 답을 join 시켜 출력

- input: string sequence (str)
- output: string sequence (str)
- purpose: remove duplicated string from input sequence and order as alphabetical order
"""

from collections import Counter


def remove_duplicate(seq: str):
    # counter: sequence string and its frequency
    # seen: set of seen alphabets (중복없는 집합)
    # stack: stack 구조 [] (리스트)
    counter, seen, stack = Counter(seq), set(), []
    for char in seq:
        counter[char] -= 1
        if char in seen:  # seen set 이미 있으면 다음 char 넘어가기
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            # char < stack[-1] : 스택의 맨 마지막 값, top element 과 비교
            # counter[stack[-1]] > 0 : 중복된 값인 경우
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)


if __name__ == '__main__':
    sequence = input('Enter string: ')
    print(remove_duplicate(sequence))
