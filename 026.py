from collections import deque
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
    edges[B].append(A)

def bfs(edges,start,N):
    seen = [False] * N
    que = deque()
    que.append(start)
    dist = [1] * N
    while que:
        now = que.popleft()
        seen[now] = True
        for next in edges[now]:
            if not seen[next]:
                que.append(next)
                dist[next] = dist[now] + 1
                seen[next] = True
    return dist


dist = bfs(edges,0,N)

odd = []
even = []
for i in range(N):
    if dist[i] % 2 == 0:
        even.append(i+1)
    else:
        odd.append(i+1)
if len(odd) >= N//2:
    print(*odd[:N//2],sep=" ")
else:
    print(*even[:N//2],sep=" "  )