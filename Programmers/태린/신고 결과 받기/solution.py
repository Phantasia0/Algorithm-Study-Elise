def solution(id_list, report, k):
    answer = []
    arr_a = {id:set() for id in id_list}
    arr_b = {id:set() for id in id_list}
    banned_id = set()

    for str in report:
        a, b = str.split(' ')
        arr_a[b].add(a)
        arr_b[a].add(b)

    for i in arr_a:
        if len(arr_a[i]) >= k:
            banned_id.add(i)

    for j in arr_b:
        answer.append(0)
        for l in arr_b[j]:
            if l in banned_id:
                answer[-1] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# [2,1,1,0]