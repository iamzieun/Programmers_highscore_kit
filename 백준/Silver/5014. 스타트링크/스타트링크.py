from sys import stdin
from collections import deque


def bfs(F, S, G, U, D):
    deq = deque()
    deq.append(S)
    
    visited = [0 for floor in range(F + 1)]
    count = [0 for floor in range(F + 1)]

    while deq:
        if G in deq:
            return count[G]
        
        current = deq.popleft()
        visited[current] = 1

        for floor in (current + U, current - D):
            if 1 <= floor <= F and visited[floor] == 0:
                visited[floor] = 1
                count[floor] = count[current] + 1
                deq.append(floor)
    
    return "use the stairs"


def main():
    F, S, G, U, D = map(int, stdin.readline().split())
    print(bfs(F, S, G, U, D))


if __name__ == '__main__':
    main()