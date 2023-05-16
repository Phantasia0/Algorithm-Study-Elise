def solution(sizes):
    big=[]
    small=[]
    for i in sizes:
        if i[0]>i[1]: # 가로가 세로보다 클때
            big.append(i[0]) #큰 값(가로) 저장 
            small.append(i[1])
        else:         # 가로가 세로보다 작을때
            big.append(i[1]) #큰 값(세로) 저장 
            small.append(i[0])
            
    return max(big)*max(small)