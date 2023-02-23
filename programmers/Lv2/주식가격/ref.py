from collections import deque

def solution(prices):
    prices = deque(prices)
    res = []
    while prices:
        key = prices.popleft()
        answer = 0
        for x in prices:
            answer += 1
            if x < key:
                break
        res.append(answer)
    return res

# https://school.programmers.co.kr/learn/courses/30/lessons/42584