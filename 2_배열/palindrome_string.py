"""
palindrome_string.py: check whether it is palindrome, using string feature, 문자열 속성 활용

- input: string sequence (str)
- output: palindrome or not (bool)
- purpose: find whether the input sequence of numbers are palindrome by slicing input sequence and using re
"""

import re


def palindrome_string(data: str) -> bool:
    data = data.lower()
    data = re.sub('[a-z0-9]', '', data)  # re 정규표현식을 이용해서 영문 알파벳과 숫자가 아닌 문자 모두 공백으로 대체
    '''
    re: 복잡한 문자열 속 특정 규칙으로 된 문자열 검색 후 변경
    - sub: 패턴과 일치되는 부분 다른 문자로 변경
    - sub(패턴, 변경하고자 하는 문자, 대상의 원본데이터
    '''
    return data == data[::-1]  # [::-1]: 역순으로 처리하는 인덱싱 기법
    # 역순 데이터와 원본 데이터가 같은지 확인


if __name__ == '__main__':
    data = input('Input sequence:')
    print(f'Is it Palindrome?', palindrome_string(data))