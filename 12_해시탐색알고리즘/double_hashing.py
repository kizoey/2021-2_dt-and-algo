"""
double_hasing: 이중해싱
"""


class HashTable:
    def __init__(self, size):
        self.hTable = [None for _ in range(size)]
        self.hData = [None] * size
        self.N = 0
        self.size = size

    def Simple_hash(self, keys):
        return keys % self.size

    def input(self, keys, value):
        init = self.Simple_hash(keys)
        i = init
        second = 11 - (keys % 11)  # 이중해싱 적용
        j = 0
        while True:
            if self.hTable[i] == None:
                self.hTable[i] = keys
                self.hData[i] = value
                self.N += 1
                return
            # keys는 동일하고, value만 변경된 경우
            if self.hTable[i] == keys:
                self.hData[i] = value
                return
            # 충돌이 발생된 경우
            j += 1
            i = (init + j * second) % self.size
            if self.N > self.size:
                break

    def show(self):
        for index, value in enumerate(zip(self.hTable, self.hData)):
            if value is not None:
                print(index, value)


if __name__ == '__main__':
    double = HashTable(17)
    double.input(100, 'rose')
    double.input(200, 'tulip')
    double.input(150, 'lily')
    double.input(90, 'peony')
    double.input(300, 'mum')
    double.input(120, 'lotus')
    double.input(240, 'hydrangea')
    double.input(250, 'paperwhite')
    double.input(260, 'lilac')
    double.show()