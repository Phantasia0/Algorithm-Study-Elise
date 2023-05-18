import math
def solution(fees, records):
    answer = []
    car = {}

    def convertM(time):
        h,m = list(map(int, time.split(':')))
        return m + ( h * 60 )
    
    def cal(fees, time):
        if fees[0] >= time:
            return fees[1]
        
        return fees[1] + (math.ceil((time - fees[0]) / fees[2]) * fees[3])

    for i in records:
        t, n, s = i.split()
        if n not in car:
            car[n] = {'IN':0, 'total':0}
        if s == 'IN':
            car[n]['IN'] = convertM(t)
        else:
            car[n]['total'] += convertM(t) - car[n]['IN']
            car[n]['IN'] = 0
    
    car = dict(sorted(car.items()))
    for j in car:
        if car[j]['IN'] > 0 or car[j]['total'] == 0:
            e = convertM('23:59')
            car[j]['total'] += e - car[j]['IN']
        answer.append(cal(fees, car[j]['total']))
            
    return answer


print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
))