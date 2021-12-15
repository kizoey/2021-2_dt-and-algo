"""
kruskal_disjoint: Kruskal 알고리즘을 이용해서 disjoint set 탐색
"""


class DisjointSet:
    def __init__(self, n):
        self.p = {}
        self.rank = {}
        for i in range(n):
            self.p[i] = i
            self.rank[i] = 0

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def union(self, first, second):
        # 정보갱신 시 작은 값을 기준으로 갱신
        if self.rank[first] > self.rank[second]:
            self.p[second] = first
        else:
            self.p[first] = second
            if self.rank[first] == self.rank[second]:
                self.rank[second] += 1


def kruskal_f(n, info):
    min_w = 0
    disjointset = DisjointSet(n)
    result = []
    for data in sorted(info, key=lambda cost: cost[2]):
        v, u, w = data
        first = disjointset.find(v)
        second = disjointset.find(u)
        if first != second:
            disjointset.union(first, second)
            result.append(data)
            min_w += data[2]
    return result, min_w