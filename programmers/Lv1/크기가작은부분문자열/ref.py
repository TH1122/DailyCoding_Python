def solution(t, p):
    return sum([ 1 for x in list(map(lambda x: t[x:x+len(p)], range(len(t)-len(p)+1))) if int(x) <= int(p)])

# https://school.programmers.co.kr/learn/courses/30/lessons/147355