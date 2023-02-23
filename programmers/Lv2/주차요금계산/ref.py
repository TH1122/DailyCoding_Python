from math import ceil

def solution(fees, records):
    res = {}
    temp = []
    for x in records:
        key = x.split(' ')
        if key[2] == 'IN':
            if key[1] in res:
                res[key[1]] -= (int(key[0][:2])*60+int(key[0][3:]))
            else:
                res[key[1]] = -(int(key[0][:2])*60+int(key[0][3:]))
            temp.append(key[1])
        else:
            res[key[1]] += (int(key[0][:2])*60+int(key[0][3:]))
            temp.remove(key[1])
    while temp:
        number = temp.pop()
        res[number] += 23*60+59
    keys = sorted(res.keys())
    def cal(num):
        return fees[1] + ceil((num-fees[0])/fees[2])*fees[3] if num > fees[0] else fees[1]
    return [ cal(res[x]) for x in keys]

# https://school.programmers.co.kr/learn/courses/30/lessons/92341