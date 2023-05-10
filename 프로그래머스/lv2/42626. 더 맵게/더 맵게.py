from heapq import heappush, heappop

def solution(scoville, K):
    
    heap = []
    for s in scoville:
        heappush(heap, s)
    
    answer = 0
    
    while heap[0] < K:
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, a + b * 2)
        answer += 1
        if answer == len(scoville) - 1 and heap[0] < K:
            return -1

    return answer