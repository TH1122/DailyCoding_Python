def solution(n, computers):
    visited = [ 0 for x in range(n)]
    res = {}
    
    def check(index, base):
        if visited[index]:
            return
        else:
            if index == base:
                res[index] = []
            visited[index] = 1
            key = computers[index]
            for i in range(n):
                if i != index and key[i]:
                    res[base].append(i)
                    check(i, base)
            return
    for m in range(n):
        check(m,m)
    return len(res.keys())

# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3#
