from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        price = prices.popleft()
        not_fall = 0
        for n_price in prices:
            if n_price >= price:
                not_fall += 1
            else:
                not_fall += 1
                break
        answer.append(not_fall)

    return answer