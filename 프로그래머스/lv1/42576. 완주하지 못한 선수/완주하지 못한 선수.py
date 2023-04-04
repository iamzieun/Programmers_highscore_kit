from collections import Counter

def solution(participant, completion):
    part_counter = Counter(participant)
    comp_counter = Counter(completion)
    
    for runner in comp_counter.keys():
        if part_counter[runner] > comp_counter[runner]:
            return runner
        del part_counter[runner]
    return list(part_counter.keys())[0]