from heapq import heappush, heappop, nlargest, heapify

def solution(operations):
    heap = []
    
    for opr in operations:
        if opr[0] == 'I':
            heappush(heap, int(opr[2:]))
        elif opr == 'D -1' and heap:
                heappop(heap)
        elif opr == 'D 1' and heap:
            heap = nlargest(len(heap), heap)[1:]
            heapify(heap)
        print(heap)
    
    if len(heap) > 0:
        answer = [nlargest(len(heap), heap)[0], heappop(heap)]
    else:
        answer = [0,0]
    return answer