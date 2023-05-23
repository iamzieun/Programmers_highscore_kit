from collections import deque

def can_convert(begin, target):
    count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]: 
            count += 1
        if count > 1: 
            return False
    return count == 1

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    queue = deque([(0, begin)])
    visited = [False] * len(words)
    
    while len(queue) > 0:
        count, word = queue.popleft()
        
        if word == target:
            return count
        
        for i in range(len(words)):
            if not visited[i] and can_convert(word, words[i]):
                count += 1
                queue.append((count, words[i]))
                visited[i] = True
                
    return 0