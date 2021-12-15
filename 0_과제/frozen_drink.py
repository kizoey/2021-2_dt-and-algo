"""
min_construction_cost.py: 음료수 얼려 먹기 프로그램 (탐색 알고리즘, DFS 적용)
- N*M 크기의 얼음 틀이 주어지는 경우, 0은 얼음틀 구멍을 1은 칸막이를 표현, 0으로 연결된 묶음을 얼린 음료수 1개로 간주
- 첫 번째 입력은 N과 M, 1 ~ 1000 사이의 자연수
- 두 번째 입력은 얼음 틀 형태가 주어짐
"""

def frozen_drink(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False  # 주어진 범위 벗어날시 종료

    if map_ice[x][y] == 0:  # 현재 노드를 아직 방문하지 않으면
        map_ice[x][y] = 1  # 방문 처리
        # 상하좌우 위치 재귀호출
        frozen_drink(x-1, y)
        frozen_drink(x, y-1)
        frozen_drink(x+1, y)
        frozen_drink(x, y+1)
        return True
    return False


if __name__ == "__main__":
    n, m = map(int,input("enter size >> ").split())  # 얼음틀 사이즈 n*m
    map_ice = []
    for i in range(n):
        map_ice.append(list(map(int,input("0 or 1 >> "))))  # 사이즈에 맞는 얼음틀 모양

    # 모든 위치에 대해 음료 얼리기
    result = 0
    for i in range(n):
        for j in range(m):
            if frozen_drink(i, j) == True:
                result += 1
    print(result)