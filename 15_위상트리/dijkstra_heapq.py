"""
dijkstra_heapq: heapq 모듈을 사용한 Dijkstra 알고리즘 구현
   - 시작과 끝점이 주어진 상태
"""
from heapq import *
from collections import defaultdict


def dijkstra(D, s, t):
    g = defaultdict(list)  # list형 dict 생성, 존재하지않은 key가 주어지면 새로 생성
    for l, r, c in D:
        g[l].append((c, r))

    q, seen, mins = [(0, s, ())], set(), {s: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
    return float("inf")


if __name__ == "__main__":
    D = [
        ("0", "1", 1), ("0", "2", 4),
        ("1", "0", 1), ("1", "2", 2),
        ("2", "0", 4), ("2", "1", 2),
        ("2", "3", 1),
        ("3", "2", 1), ("3", "4", 8),
        ("3", "5", 3),
        ("4", "3", 8), ("4", "5", 4),
        ("5", "3", 3), ("5", "4", 4)
    ]
    print("=== Dijkstra ===")
    print("0 -> 4:")
    print(dijkstra(D, "0", "4"))
    print("0 -> 5:")
    print(dijkstra(D, "0", "5"))