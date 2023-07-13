import math 
from collections import deque

def solution(progresses, speeds):
    day_queue = deque([math.ceil((100 - progresses[idx]) / speeds[idx]) for idx in range(len(progresses))] + [100])
    
    temp = day_queue.popleft()
    count = 1
    answer = []
    
    while day_queue:
        if temp < day_queue[0]:
            answer.append(count)
            temp = day_queue.popleft()
            count = 1
        else:
            day_queue.popleft()
            count += 1
        
        
    print(day_queue, answer)
    
    return answer