from collections import Counter

def solution(participant, completion):
    part_counter, comp_counter = Counter(participant), Counter(completion)
    
    for runner in comp_counter.keys():
        if part_counter[runner] > comp_counter[runner]:
            return runner
        del part_counter[runner]
    return list(part_counter.keys())[0]