def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer