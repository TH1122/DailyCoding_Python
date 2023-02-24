from itertools import combinations

def solution(orders, course):
    res = []
    for length in course:
        condition = set([])
        for i in orders:
            condition |= set(combinations(i, length))
        if condition:
            temp = []
            maximum = 2
            for sub in condition:
                count = 0
                sub = set(sub)
                for target in orders:
                    if sub.issubset(target):
                        count += 1
                if count > maximum:
                    maximum = count
                    temp = [''.join(sorted(sub))]
                elif count == maximum:
                    temp.append(''.join(sorted(sub)))
            res += list(set(temp))
    return sorted(res)

# https://school.programmers.co.kr/learn/courses/30/lessons/72411