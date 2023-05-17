from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 이동할 네 방향 정의 (좌, 우, 상, 하)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        
        deq = deque()
        deq.append((x, y))
        
        # deq가 빌 때까지 반복
        while deq: 
            x, y = deq.popleft()
            
            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵을 벗어난 경우 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                    
                # 벽인 경우 무시
                if maps[nx][ny] == 0:
                    continue
                
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    deq.append((nx, ny))
                
                #print(maps)
                
        if maps[n-1][m-1] == 1:
            maps[n-1][m-1] = -1
            
        return maps[n-1][m-1]
        
    return bfs(0, 0)