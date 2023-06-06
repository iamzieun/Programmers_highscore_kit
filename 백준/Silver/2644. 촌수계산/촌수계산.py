from sys import stdin
from collections import defaultdict, deque


def BFS(graph, node, visited):
    queue = deque([node]) 
    while queue:                                    # 큐가 빌 때까지
        node = queue.popleft()                      # 큐에서 node(=현재 노드)를 꺼내요
        for n in graph[node]:                       # 현재 노드와 인접한 노드들 중
            if visited[n] == 0:                     # 아직 방문하지 않았다면
                visited[n] = visited[node] + 1      # 방문처리를 하고 (현재 노드까지의 이동 거리 + 1)
                queue.append(n)                     # 큐에 넣습니다


def main():
    n = int(stdin.readline())
    p1, p2 = map(int, stdin.readline().split())
    m = int(stdin.readline())
    people = [list(map(int, stdin.readline().split())) for _ in range(m)]
    graph = defaultdict(list)
    for u, v in people:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0 for i in range(n + 1)]
    BFS(graph, p1, visited)

    print(int(visited[p2] if visited[p2] > 0 else -1))


if __name__ == '__main__':
    
    main()