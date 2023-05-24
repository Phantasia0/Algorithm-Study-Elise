import sys
input = sys.stdin.readline

# input  Nx2 행렬
N = int(input())
D = [[0 for column in range(2)] for row in range(N+1)]

# 첫번째 자리 초기화
D[1][0] = 0  
D[1][1] = 1 

# 두번째 자리부터 N자리 까지 점화식을 사용하여 구한다
for i in range(2, N+1):
    D[i][0] = D[i-1][0] + D[i-1][1] # 0이 될 수있는 경우
    D[i][1] = D[i-1][0]             # 1이 될 수있는 경우

print(D[N][0]+ D[N][1]) # N자리에서 0과 1이 되는 모든 경우의 수
