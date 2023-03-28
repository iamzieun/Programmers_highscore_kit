import itertools

def solution(numbers):
    answer = 0
    
    # 종이 조각 list
    a_list = list(numbers)
    
    # 종이 조각 조합
    b_list = []
    for i in range(1, len(numbers) + 1):
        b_list += list(itertools.permutations(a_list, i))
    
    # 조합한 종이 조각 숫자로 변환
    c_list = [int("".join(j)) for j in b_list]
    c_list = list(set(c_list))  # 중복 제거
    
    # 소수 판별
    n_list = []
    
    for n in c_list:
        status = True
        if n < 2:
            status = False
        for l in range(2, int(n ** 0.5) + 1):
            if n % l == 0:
                status = False
                break
        if status == True:
            n_list.append(n)
            
    answer = len(n_list)
    
    return answer