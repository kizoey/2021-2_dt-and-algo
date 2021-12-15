class HashTable:
    def __init__(self, size):
        self.hTable = [None for _ in range(size)]

    def mySimple_hash(self, keys):
        sum = 0
        for key in keys:
            sum += ord(key)  # 아스키값 사용
        return sum % len(self.hTable)  # 제산함수 적용

    def input(self, keys, value):
        self.hTable[self.mySimple_hash(keys)] = value

    def show(self):
        for index, value in enumerate(self.hTable):
            if value is not None:
                print(index, value)

    def search(self, keys):
        return self.hTable[self.mySimple_hash(keys)]

    # Honer's rule 적용, HashTable 클래스의 메서드
    def simple_honer(self, keys):
        honer = 26
        sum = 0
        for key in keys:
            sum += sum * honer + ord(key)
        return sum % len(self.hTable)


if __name__ == '__main__':
    member = HashTable(50)
    member.input('choi', 7367)
    member.input('lee', 3380)
    member.input('park', 4522)
    member.input('kim', 9622)
    member.show()
    print(member.search('park'))