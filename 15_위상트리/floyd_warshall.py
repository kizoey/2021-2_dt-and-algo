"""
floyd_warshal: Floyd-Wharshall 알고리즘으로 위상트리 탐색
"""
import sys

def floyd_warshall(g):
    n = len(g)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    for i in range(n):
        if g[i][i] < 0:
            print(f'graph contains a negative cycle')

    for i in range(n):
        for j in range(n):
            print(f'{g[i][j]:4d}', end=' ')
        print()


if __name__ == "__main__":
    INF = sys.maxsize
    g = [[0, 4, 5, INF, INF, INF],
         [INF, 0, -2, INF, INF, INF],
         [INF, INF, 0, 3, INF, INF],
         [INF, INF, INF, 0, 4, -1],
         [INF, INF, INF, INF, 0, 4],
         [INF, INF, INF, -2, INF, 0]]