# 10번 케이스 시간초과
def solution(number, k):
    answer = []
    n_lst = list(str(number))
    n_len = len(n_lst)
    idx = 0
    
    for i in range(n_len - k):
        max_idx = idx
        for j in range(idx, k + i + 1):
            if n_lst[j] == '9':
                max_idx = j
                break
            elif n_lst[j] > n_lst[max_idx]:
                max_idx = j
        
        answer.append(n_lst[max_idx])
        idx = max_idx + 1

    answer = "".join(answer)
    return answer