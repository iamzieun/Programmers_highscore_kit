def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]  # 다리를 건너는 트럭
    
    while bridge:
        answer += 1
        bridge.pop(0)   # 맨 앞의 트럭은 다리를 다 건넘
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                truck_weights.pop(0)  
            else:
                bridge.append(0)
        
    return answer