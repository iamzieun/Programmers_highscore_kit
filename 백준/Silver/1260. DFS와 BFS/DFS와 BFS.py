# 1260번: DFS와 BFS
# https://www.acmicpc.net/problem/1260

from sys import stdin
from collections import defaultdict, deque


def dfs(N, V, graph):
    stack = [V]
    visited = [0 for _ in range(N + 1)]
    route = [V]

    while stack:
        current = stack.pop()

        if visited[current] == 0:
            route.append(current)
            visited[current] = 1

            for neighbor in sorted(graph[current], reverse=True):  # 이 부분 수정
                if visited[neighbor] == 0:
                    stack.append(neighbor)

    answer = " ".join(map(str, route[1:]))
    print(answer)


def bfs(N, V, graph):
    deq = deque([V])
    visited = [0 for _ in range(N + 1)]
    visited[V] = 1
    route = [V]

    while deq:
        current = deq.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == 0:
                route.append(neighbor)
                visited[neighbor] = 1
                deq.append(neighbor)
    
    answer = " ".join(map(str, route))
    print(answer)


def main():
    N, M, V = map(int, stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for n in range(1, N+1):  # 수정된 부분
        graph[n] = sorted(graph[n])

    dfs(N, V, graph)
    bfs(N, V, graph)


if __name__ == "__main__":
    main()