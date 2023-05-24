def max_sum(a, b, c): # 평균값과 중앙값 차이
    #(a+b+c)/3-b  => a+b+c-3*b 
    return abs(a+b+c-3*b)

# input
N = int(input())  # N = int(sys.stdin.readline())
# N회 입력받기
num_list = [int(input()) for _ in range(N)]
# num_list = []
# for _ in range(N): num_list.append(int(input()))
num_list.sort()

answer=0

for i in range(1, N-1):
    answer = max(answer, max_sum(num_list[i-1], num_list[i], num_list[N-1]))# 평균이 최대
    answer = max(answer, max_sum(num_list[0], num_list[i], num_list[i+1]))  # 평균이 최소

print(answer)