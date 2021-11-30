"""
palindrome_list.py: check whether it is palindrome, using list, 리스트 활용

- input: string sequence (str)
- output: palindrome or not (bool)
- purpose: find whether the input sequence of numbers are palindrome, 회문/앞뒤가 똑같은 문자열
"""


def palindrome_list(data: str) -> bool:
    string_lst = []
    for char in data:
        if char.isalpha():  # isalpha: 각 문자열이 알파벳인지 확인
            string_lst.append(char.lower())  # string_lst append lowered character
        print(string_lst)
    while len(string_lst) > 1:
        if string_lst.pop(0) != string_lst.pop():
            return False
    return True


if __name__ == '__main__':
    data = input('Input sequence:')
    print(f'Is it Palindrome?', palindrome_list(data))