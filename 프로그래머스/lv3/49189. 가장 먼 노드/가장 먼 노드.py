def solution(n, edge):
    edge.sort()

    # 각 노드에 연결된 노드
    graph = [[] for _ in range(n + 1)]  
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    #print("graph: ", graph)
    
    # 1번 노드로부터의 거리
    distance = [0] * (n + 1)
    distance[1] = 1
    
    # 앞으로 갈 노드들
    queue = [1]
    
    while queue:
        curr_node = queue.pop(0)
        for next_node in graph[curr_node]:
            if distance[next_node] == 0:
                distance[next_node] = distance[curr_node] + 1
                queue.append(next_node)
                #print("queue", queue)
    
    return distance.count(max(distance))
            
    
    #return answer