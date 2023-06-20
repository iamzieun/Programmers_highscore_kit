def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = 0
    for idx, i in enumerate(citations):
        if i >= idx + 1:
            answer = idx + 1
    return answer