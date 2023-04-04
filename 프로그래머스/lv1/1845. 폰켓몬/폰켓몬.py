from collections import Counter

def solution(nums):
    counter = Counter(nums)
    if len(nums) // 2 <= len(counter): answer = len(nums) // 2
    else: answer = len(counter)
    return answer