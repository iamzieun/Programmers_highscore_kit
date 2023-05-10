from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    start = -1
    now = 0
    cleared = 0
    heap = []
    
    while cleared < len(jobs):

        # 현재 수행 가능한 작업들
        for job in jobs:
            if start < job[0] and job[0] <= now:
                # 작업의 소요시간, 작업이 요청되는 시점
                heappush(heap, [job[1], job[0]])    
        
        # 현재 수행 가능한 작업이 있는 경우
        if heap:
            current = heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            cleared += 1
        
        # 현재 수행 가능한 작업이 없는 경우 1초동안 놀기
        else:
            now += 1
            
    return answer // len(jobs)