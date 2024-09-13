from collections import deque

N, M, V = map(int, input().split())
link = [list(map(int, input().split())) for _ in range(M)]

adjl = [[] for _ in range(N+1)]
for i in range(M):
    adjl[link[i][0]].append(link[i][1])
    adjl[link[i][1]].append(link[i][0])

# DFS - stack
for a in adjl:
    a.sort(reverse=True)

stack = [V]
visited = [0] * (N+1)
dfs_result = []
while stack:
    t = stack.pop()

    for i in range(len(adjl[t])):
        if visited[adjl[t][i]] == 0:
            stack.append(adjl[t][i])
    else:
        if t not in dfs_result:
            dfs_result.append(t)
            visited[t] = 1

print(*dfs_result)

# BFS - queue
for a in adjl:
    a.sort()

q = deque([V])
visited = [0] * (N + 1)
bfs_result = []
while q:
    f = q.popleft()

    for i in range(len(adjl[f])):
        if visited[adjl[f][i]] == 0:
            q.append(adjl[f][i])
    else:
        if f not in bfs_result:
            bfs_result.append(f)
            visited[f] = 1

print(*bfs_result)