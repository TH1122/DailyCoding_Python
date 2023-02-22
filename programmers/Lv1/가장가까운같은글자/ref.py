def solution(s):
    def check(target):
        res = -1
        target = list(reversed(target))
        if target[0] in target[1:]:
            res = target[1:].index(target[0])+1
        return res
    return [check(s[0:idx]) for idx in range(1,len(s)+1)]

# https://school.programmers.co.kr/learn/courses/30/lessons/142086
