def solution(triangle):
    answer = 0
    row = len(triangle) # 삼각형의 층수
    result = [0] * row  # 메모이제이션을 위한 메모리 할당

    for i in range(row):
        for j in reversed(range(i+1)):  # 순서대로 갱신할 경우 갱신된 값을 이용해 갱신하므로 역순 반복
            if j == 0:                  # 처음과 끝은 항상 직전 층의 처음과 끝과의 합
                result[j] += triangle[i][j]
            elif j == i:
                result[j] = result[j-1] + triangle[i][j]
            else:                       # 직전 층의 앞뒤 계산 결과 중 큰 값으로 연산
                result[j] = triangle[i][j] + max(result[j-1], result[j])
            
    answer = max(result)

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))