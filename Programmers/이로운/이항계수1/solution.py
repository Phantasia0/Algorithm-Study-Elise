import sys
input = sys.stdin.readline

N, K = map(int, input().split())
D = [[0 for column in range(N+1)] for row in range(N+1)]

for i in range(0, N+1):
    D[i][1] = i # iC1 = i
    D[i][0] = 1 # iC0 = 1
    D[i][i] = 1 # iCi = 1

for i in range(2, N+1):
    for j in range(1, N):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
    #이전상태에서 (선택이 다 된경우) + (선택이 하나 남은경우) 

print(D[N][K])