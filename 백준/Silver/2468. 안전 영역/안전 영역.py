from sys import stdin
from collections import deque


# 동서남북
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(r, c, N, G):
    deq = deque()
    deq.append((r, c))

    while deq: 
        r, c = deq.popleft()
        G[r][c] = 1

        for idx in range(4):
            nr, nc = r + dr[idx], c + dc[idx]
            
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            
            # if G[nr][nc] == 1 or G[nr][nc] == -1:    # 이미 방문한 곳이거나 물에 잠긴 곳이면
            #     continue

            if G[nr][nc] == 0:
                G[nr][nc] = 1
                deq.append((nr, nc))


def main():
    N = int(stdin.readline())
    two_dim_G = [list(map(int, stdin.readline().split())) for _ in range(N)]
    one_dim_G = [element for sublist in two_dim_G for element in sublist]

    high, low = max(one_dim_G), min(one_dim_G)
    
    if high == low:
        return 1
    
    not_sinked = []
    for height in range(low, high):                         # 강수량에 따라
        G = [-1 if h <= height else 0 for h in one_dim_G]   # 잠긴 곳은 -1, 안 잠긴 곳은 0 
        G = [G[i:i+N] for i in range(0, len(G), N)]

        count = 0                                           # 안전한 영역의 경우의 수
        for r in range(N):                                  # 각 위치에서
            for c in range(N):
                if G[r][c] == 0:                            # 안 잠긴 곳이면
                    bfs(r, c, N, G)                         # 그 곳과 연결된 곳을 방문처리
                    count += 1

        not_sinked.append(count)

    return max(not_sinked)


if __name__ == "__main__":
    result = main()
    print(result)