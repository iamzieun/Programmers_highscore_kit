from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    
    while prices:
        price = prices.popleft()
        not_fall = 0
        for n_price in prices:
            not_fall += 1
            if n_price >= price: continue
            else: break
        answer.append(not_fall)

    return answer