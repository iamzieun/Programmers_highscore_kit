# 2178: 미로 탐색
# https://www.acmicpc.net/problem/2178

from sys import stdin
from collections import deque


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

deq = deque()
deq.append((0, 0))

def dfs(N, M, G):
    x, y = deq.popleft()

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if G[nx][ny] == 0:
            continue

        if G[nx][ny] == 1:
            G[nx][ny] = G[x][y] + 1
            deq.append((nx, ny))


def main():
    N, M = map(int, stdin.readline().split())
    G = []
    for _ in range(N):
        digit = stdin.readline().strip()
        digits = [int(d) for d in digit]
        G.append(digits)

    while deq:
        dfs(N, M, G)

    print(G[N-1][M-1])


if __name__ == '__main__':
    main()