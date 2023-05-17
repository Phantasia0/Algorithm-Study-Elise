def solution(n, info):
    answer = [-1]
    lion = [0] * 11
    maxD = 0

    def comparePoint(lion):
        lion_total = 0
        apeach_total = 0
        nonlocal maxD, answer
        for p in range(10):
            if lion[p] > info[p]:
                lion_total += 10-p
            elif info[p]:
                apeach_total += 10-p
        result = lion_total - apeach_total
        if maxD < result:
            maxD = result
            answer = lion
        elif maxD == result and result > 0:
            if answer[0] == -1:
                answer = [0] * 11
            for i in range(10, -1, -1):
                if lion[i] > 0:
                    if lion[i] > answer[i]:
                        answer = lion
                        return
                    elif lion[i] == answer[i]:
                        continue
                if answer[i] > 0:
                    return

    def getPoint(arrow, lion, stage):
        if stage == 10:
            lion[stage] = arrow
            arrow = 0
        # 화살이 남았는지 체크
        if arrow == 0:
            comparePoint(lion)
            return
        # 화살 쏘고 호출
        if arrow > info[stage]:
            next_arrow = arrow-info[stage]-1
            next_lion = lion[:]
            next_lion[stage] = info[stage] + 1
            getPoint(next_arrow, next_lion, stage+1)
        # 안쏘고 호출
        getPoint(arrow, lion, stage+1)
        return
    
    getPoint(n, lion, 0)
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))