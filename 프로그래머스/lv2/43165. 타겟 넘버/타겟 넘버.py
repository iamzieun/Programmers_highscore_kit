from collections import deque

def solution(numbers, target):
    answer = 0
    deq = deque()
    n = len(numbers)
    
    deq.append([numbers[0], 0])
    deq.append([-1 * numbers[0], 0])
    
    while deq:
        temp, idx = deq.popleft()
        idx += 1
        if idx < n:
            deq.append([temp + numbers[idx], idx])
            deq.append([temp - numbers[idx], idx])
        elif temp == target:
            answer += 1
        # print(deq)
    
    return answer