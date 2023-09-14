from collections import deque

N = int(input())

G = [[] for _ in range(N)]

for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

def bfs(n):
    Q = deque()
    dist = [-1]*N
    dist[n] = 0
    Q.append(n)
    arr = [0,0]
    while Q:
        i = Q.popleft()
        for j in G[i]:
            if dist[j] == -1:
                a = dist[i] + 1
                dist[j] = a
                Q.append(j)
                if a > arr[1]:
                    arr = [j,a]
    return arr

p,dep = bfs(0)
q,dep2 = bfs(p)

print(dep2+1)
