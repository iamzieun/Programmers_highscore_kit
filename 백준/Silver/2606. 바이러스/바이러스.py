# 2606번: 바이러스
# https://www.acmicpc.net/problem/2606

from sys import stdin
from collections import defaultdict, deque


def BFS(graph, visited):
    queue = deque([1]) 
    while queue:                                    # 큐가 빌 때까지
        node = queue.popleft()                      # 큐에서 node(=현재 노드)를 꺼내요
        for n in graph[node]:                       # 현재 노드와 인접한 노드들 중
            if visited[n] == 0:                     # 아직 방문하지 않았다면
                visited[n] = 1                      # 방문처리를 하고 (현재 노드까지의 이동 거리 + 1)
                queue.append(n)                     # 큐에 넣어요


def main():
    n = int(stdin.readline())                                                   # 컴퓨터의 수
    m = int(stdin.readline())                                                   # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
    computer = [list(map(int, stdin.readline().split())) for _ in range(m)]     # 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍
    graph = defaultdict(list)
    for u, v in computer:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0 for i in range(n + 1)]
    BFS(graph, visited)

    print(sum(visited) - 1)


if __name__ == '__main__':
    
    main()