# 9205번: 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

from sys import stdin
from collections import deque

def distance(r, c, nr, nc):
    return abs(nr - r) + abs(nc - c)


def bfs(home_r, home_c, festival_r, festival_c, n, G):
    deq = deque()
    deq.append((home_r, home_c))
    visited = [0 for _ in range(n)]
    
    while deq:
        r, c = deq.popleft()
        
        if distance(r, c, festival_r, festival_c) <= 1000:
            return "happy"
        
        for i in range(n):
            nr, nc = G[i]
            if visited[i] == 0 and distance(r, c, nr, nc) <= 1000:
                deq.append((nr, nc))
                visited[i] = 1

    return "sad"


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        home_r, home_c = map(int, stdin.readline().split())
        G = [list(map(int, stdin.readline().split())) for _ in range(n)]
        festival_r, festival_c = map(int, stdin.readline().split())
        print(bfs(home_r, home_c, festival_r, festival_c, n, G))


if __name__ == '__main__':
    main()