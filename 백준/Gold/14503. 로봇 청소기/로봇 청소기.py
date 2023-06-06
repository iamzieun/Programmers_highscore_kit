# 14503번: 로봇 청소기
# https://www.acmicpc.net/problem/14503

from sys import stdin


# 북(0) 동(1) 남(2) 서(3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def turn_left(d):
    return (d + 3) % 4

def dfs(r, c, d, G):
    # 현재 위치 청소
    if G[r][c] == 0:                        # 1. 현재 칸이 아직 청소되지 않은 경우,
        G[r][c] = 2                         #    현재 칸을 청소한다
        cleaned = 1
    else:
        cleaned = 0
    
    # 주변 4칸 확인
    for neigh in range(4):                  # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        d = turn_left(d)                    #    반시계 방향으로 90도 회전한다.
        if G[r + dr[d]][c + dc[d]] == 0:    #    바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우
            r += dr[d]                      #    한 칸 전진한다
            c += dc[d]                      
            cleaned += dfs(r, c, d, G)      #    1번으로 돌아간다
            return cleaned

                                            # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if G[r - dr[d]][c - dc[d]] != 1:        #    바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 
        r -= dr[d]                          #    한 칸 후진하고
        c -= dc[d]
        cleaned += dfs(r, c, d, G)          #    1번으로 돌아간다.
        
    return cleaned                          # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.


def main():
    N, M = map(int, stdin.readline().split())
    r, c, d = map(int, stdin.readline().split())
    G = [list(map(int, stdin.readline().split())) for _ in range(N)]

    print(dfs(r, c, d, G))


if __name__ == '__main__':
    main()