def solution(tickets):
    res = []
    
    def make(arr, route):
        if len(arr) == 0:
            res.append(route)
            return
        
        if route:
            key = route[-1]
            for m in arr:
                if m[0] == key:
                    temp_route = route.copy()
                    temp_route.append(m[-1])
                    temp_arr = arr.copy()
                    temp_arr.remove(m)
                    make(temp_arr, temp_route)
            
        else:
            for x in arr:
                if x[0] == 'ICN':
                    temp_route = x.copy()
                    temp_arr = arr.copy()
                    temp_arr.remove(x)
                    make(temp_arr, temp_route)

    make(tickets, [])
    return sorted(res)[0]

# https://school.programmers.co.kr/learn/courses/30/lessons/43164