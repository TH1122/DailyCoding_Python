def solution(n):
    def make(num):
        res = ''
        while num> 0:
            res = str(num%3) + res
            num = int(num//3)
        return res
    return int(make(n)[::-1],3)