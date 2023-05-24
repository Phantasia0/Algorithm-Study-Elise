def solution(k, d):
    answer = 0
    ak = 0
    while ak <= d: # ak를 k만큼 증가시키면서 bk의 갯수구하기
        bk = (d ** 2 - ak ** 2)**0.5   
        answer += (bk // k) + 1 # 여기서 1은 0일때 값
        ak += k
    return answer



