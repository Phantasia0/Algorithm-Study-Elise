# 예산 계산
def calculate_budget(bound : int) -> int:
    sum = 0
    for req in reqs:
        sum += min(req, bound) # bound를 상한액으로 계산
    return sum

# input
n = int(input())
reqs = list(map(int, input().split()))
budget = int(input())

low = 0
high = max(reqs)
bound = 0
answer = 0

while low <= high:
    mid = (low +high) // 2

    if (calculate_budget(mid) <= budget):
        bound = mid  # bound 정답조건 
        low = mid + 1
    else:
        high = mid - 1

budgets = []
#예산은 bound로 정해진 상한액중 가장 최대값이 정답 
for req in reqs:
    budgets.append(min(req, bound))
#budgets = list( map(lambda x: min(x, bound), reqs) ) #위와 같은식

answer=max(budgets)

#print(budgets)
print(answer)
