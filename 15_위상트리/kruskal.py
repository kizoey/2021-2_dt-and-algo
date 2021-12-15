"""
kruskal: Kruskal 알고리즘을 이용한 위상트리 탐색
"""

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    first = find(u)
    second = find(v)
    p[second] = first


def kruskal_f(n, info):
    info.sort(key=lambda cost: cost[2])
    result = []
    for i in range(n):  # 초기 정점 집합(각 정점이 개별 집합이 됨)
        p.append(i)
    tree_edges = 0  # number of edges
    min_w = 0  # sum of weight

    while True:
        if tree_edges == n - 1:
            break
        u, v, w = info.pop(0)
        if find(u) != find(v):
            union(u, v)
            result.append((u, v))
            min_w += w
            tree_edges += 1
    return result, min_w


if __name__ == "__main__":
    p = []  # 서로소집합
    info = [[0, 1, 4], [0, 2, 3], [1, 2, 2], [2, 3, 1], [3, 4, 1], [3, 5, 5], [4, 5, 6]]
    print(kruskal_f(6, info))