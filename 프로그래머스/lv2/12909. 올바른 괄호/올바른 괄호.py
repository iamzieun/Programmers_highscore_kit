def solution(s):
    answer = True
    parenthesis_lst = list(s)
    store = []
    
    for parenthesis in parenthesis_lst:
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