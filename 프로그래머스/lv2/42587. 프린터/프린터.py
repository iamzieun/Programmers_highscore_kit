from collections import deque

def solution(priorities, location):
    answer = 0
    
    priorities_lst = [(idx, priority) for idx, priority in enumerate(priorities)]
    priorities_queue = deque(priorities_lst)
    
    print_lst = []
    
    while priorities_queue:
        idx, priority = priorities_queue.popleft()
        if priorities_queue:
            n_priorities = [n_p for _, n_p in priorities_queue] # 남아있는 문서들의 우선순위
            if priority >= max(n_priorities):
                print_lst.append((idx, priority))
            else:
                priorities_queue.append((idx, priority))
        else:
            print_lst.append((idx, priority))  
    
    print(print_lst)
    
    for idx, (loc, priority) in enumerate(print_lst):
        if loc == location:
            answer = idx + 1
            break
    
    return answer