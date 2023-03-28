def solution(answers):
    answer = []
    
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i, n in enumerate(answers):
        if n == ans_1[i % 5]: 
            score[0] += 1
        if n == ans_2[i % 8]: 
            score[1] += 1
        if n == ans_3[i % 10]: 
            score[2] += 1
    
    score_max = max(score)
    answer = [i + 1 for i, n in enumerate(score) if n == score_max]

    return answer