def solution(arr):
    answer = [-1]
    for num in arr:
        if num != answer[-1]:
            answer.append(num)  
    answer.pop(0)
    return answer