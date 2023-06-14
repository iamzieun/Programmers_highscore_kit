# 2573번: 빙산
# https://www.acmicpc.net/problem/2573

import copy
from sys import stdin
from collections import deque

def timelapse(N, M, G):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    G_after = [[0] * M for _ in range(N)]
    
    for r in range(N):
        for c in range(M):
            if G[r][c] > 0:
                lower = 0
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M:
                        if G[nr][nc] == 0:
                            lower += 1
                G_after[r][c] = max(G[r][c] - lower, 0)
    
    return G_after


def bfs(r, c, N, M, G, visited):
    deq = deque()
    deq.append([r, c])
    visited[r][c] = True

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    while deq:
        r, c = deq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not visited[nr][nc] and G[nr][nc] > 0:
                visited[nr][nc] = True
                deq.append([nr, nc])


def main():
    N, M = map(int, stdin.readline().split())
    G = [list(map(int, stdin.readline().split())) for _ in range(N)]
    year = 0

    while True:
        count = 0
        visited = [[False] * M for _ in range(N)]

        for r in range(N):
            for c in range(M):
                if not visited[r][c] and G[r][c] > 0:
                    bfs(r, c, N, M, G, visited)
                    count += 1
        
        if count >= 2:
            print(year)
            return
            
        if sum([sum(G[i]) for i in range(N)]) == 0:
            print(0)
            return
            
        year += 1
        G = timelapse(N, M, G)


if __name__ == "__main__":
    main()