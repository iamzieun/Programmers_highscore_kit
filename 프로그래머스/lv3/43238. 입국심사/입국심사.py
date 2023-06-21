def solution(n, times):
    
    left, right = 1, max(times) * n     # 1분부터 가장 오래 걸리는 심사관이 n명을 검사하는데 걸리는 시간(분)까지 탐색
    
    while left < right:
        mid = (left + right) // 2
        people = 0
        for time in times:              # 각 심사관별로
            people += mid // time       # mid분동안 심사하는 사람의 수를 합친다
            if people >= n:
                break
        if people >= n:
            right = mid
        else:
            left = mid + 1
            
    return left