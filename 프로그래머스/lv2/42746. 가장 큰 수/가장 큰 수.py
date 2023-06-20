def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x * 4, reverse=True)
    return str(int("".join(numbers)))