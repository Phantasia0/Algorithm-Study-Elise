def solution(n, computers):
    answer = 0
    visited = set()
    stack = []

    def DFS():
        while stack:
            node = stack.pop()
            visited.add(node)
            for i in range(n):
                if computers[node][i] == 1 and i not in visited:
                    stack.append(i)
        return 1

    for v in range(n):
        if v not in visited:
            stack.append(v)
            answer += DFS()

    return answer
