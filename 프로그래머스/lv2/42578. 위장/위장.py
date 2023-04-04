from collections import Counter
def solution(clothes):
    answer = 1
    clothes_category = [cloth[1] for cloth in clothes]
    clothes_counter = Counter(clothes_category)
    for count in clothes_counter.values():
        answer = answer * (count + 1)
    answer = answer - 1
    return answer