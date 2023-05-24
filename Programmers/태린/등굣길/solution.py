def solution(m, n, puddles):
    answer = 0
    route = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # Index와 좌표의 값을 동일하게 쓰기 위해 +1

    route[1][1] = 1

    for y in range(1, n+1):
        for x in range(1, m+1):
            if [x, y] in puddles:
                continue
            route[x][y] += route[x-1][y] + route[x][y-1]
    answer = route[m][n] % 1000000007

    return answer

print(solution(4,3,[[2, 2]]))