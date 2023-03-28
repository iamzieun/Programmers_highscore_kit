def solution(brown, yellow):
    sqr = brown + yellow    # 전체 넓이
    
    for i in range(3, sqr // 2 + 1):
        if sqr % i == 0 and (i - 2) * (sqr // i - 2) == yellow:
            answer = [i, sqr // i]
            answer.sort(reverse=True)
            break
    
    return answer