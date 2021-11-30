"""
arraylist.py: Class of Arraylist()

- __init__: initialization of parameters (data, List[int])
- isEmpty: check len(data) == 0
- head_insert: insert element at the first of list
- insert_after: insert element at specific position
- delete_: delete element at specific position
- display: display all elements within class
"""

'''
[배열의 삽입: 배열의 포화상태 검사, 추가 가능하다면 추가 위치 이후 오른쪽으로 이동]
add 또는 insert function(ArrayList, item, p){
	if ArrayList is empty:
		Error 또는 ArrayList[0] = item
	else if ArrayList isn’t full and p >= 0 and p
		< ArrayList의 입력 size(즉, 입력갯수):
		for 입력 size – 1 에서부터 p위치까지 -1감소:
			ArrayList[i+1] = ArrayList[i]
		ArrayList[p] = item
		size +1 증가
	}
'''

'''
[배열의 삭제: 삭제할 데이터의 유무 확인, 삭제할 위치 이후 데이터 왼쪽으로 이동]
delete function(ArrayList, p){
	if ArrayList is empty and p <0 or p >= ArrayList size:
		Error
	else:
		item = ArrayList[p]
		for p에서 부터 ArrayList size -1 까지 1증가:
				ArrayList[i] = ArrayList[i+1]
			ArrayList[p] = item
			size 1 감소
	return item
	}
'''


class ArrayList:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True

    # 맨 앞에 원소 추가
    def head_insert(self, item):
        if not self.data:  # 데이터 추가가능성 판단
            self.data.append(item)
        else:
            self.data.append(None)
            size = len(self.data)
            for i in range(size, 1, -1):  # 한칸씩 왼쪽으로 이동
                self.data[i - 1] = self.data[i - 2]
            self.data[0] = item

    # 특정 위치에 원소 추가
    def insert_after(self, item, pos):
        if pos == len(self.data) - 1:  # 맨 뒤에 원소 추가하는 경우
            self.data.append(item)
        else:
            self.append(None)
            size = len(self.data)
            for i in range(size, pos + 1, -1):
                self.data[i - 1] = self.data[i - 2]
            self.data[pos] = item

    # 특정 위치의 원소 삭제
    def delete_(self, pos):
        if self.isEmpty():  # 삭제할 데이터의 유무 판단
            print(f'This list is empty.')
        else:
            self.data.pop(pos)

    def display(self):
        print(f'List of items: {self.data}')


if __name__ == '__main__':
    name = ArrayList()
    name.head_insert('name')
    name.head_insert('my')
    name.insert_after('is', 1)
    name.delete_(2)
    name.insert_after('was', 1)
    name.insert_after('zoey', 2)
    name.display()
