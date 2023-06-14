# 1697번: 숨바꼭질
# https://www.acmicpc.net/problem/1697

from sys import stdin
from collections import deque

def bfs(N, K):
    deq = deque()
    deq.append(N)
    count = [0] * (100000 + 1)

    while deq:
        current = deq.popleft()

        if current == K:
            print(count[current])
            return
        
        for location in [current - 1, current + 1, current * 2]:
            if 0 <= location <= 100000 and not count[location]:
                count[location] = count[current] + 1
                deq.append(location)
            

def main():
    N, K = map(int, stdin.readline().split())
    bfs(N, K)


if __name__ == "__main__":
    main()