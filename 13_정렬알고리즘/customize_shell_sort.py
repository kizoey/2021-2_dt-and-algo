"""
customize_shell_sort: 쉘 정렬의 간단한 버전
"""

def customize_shell(data):
    size = len(data)
    gap = size // 2
    print(gap, ', ', size)

    while gap >= 1:
        for i in range(gap, size):
            target = i
            while target >= gap and data[target - gap] > data[target]:
                data[target], data[target - gap] = data[target - gap], data[target]
                target -= gap
        gap //= 2