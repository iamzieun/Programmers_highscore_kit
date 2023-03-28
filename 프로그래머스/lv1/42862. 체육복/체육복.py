def solution(n, lost, reserve):
    
    # 도난 o 여벌 o
    lost_del = list(set(lost) - set(reserve))
    reserve_del = list(set(reserve) - set(lost))

    # 도난 x 여벌 o
    for i in lost_del:
        if i - 1 in reserve_del:
            lost_del.remove(i)
            reserve_del.remove(i - 1)
        elif i + 1 in reserve_del:
            lost_del.remove(i)
            reserve_del.remove(i + 1)
    
    answer = n - len(lost_del)
    
    return answer


def solution(n, lost, reserve):
    
    # 도난 o 여벌 o
    lost_del = list(set(lost) - set(reserve))
    reserve_del = list(set(reserve) - set(lost))

    # 도난 x 여벌 o
    for i in reserve_del:
        if i - 1 in lost_del:
            lost_del.remove(i - 1)
        elif i + 1 in lost_del:
            lost_del.remove(i + 1)
    
    answer = n - len(lost_del)
    
    return answer