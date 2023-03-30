def solution(s):
    answer = True
    store = []
    
    for parenthesis in s:
        if parenthesis == "(":
            store.append(parenthesis)
        elif len(store) > 0:
            store.pop()
            continue
        else:
            answer = False
            break
    
    if len(store) > 0:
        answer = False

    return answer