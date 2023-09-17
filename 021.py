import sys 
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
edge = [[] for _ in range(N)]

redge = [[] for _ in range(N)]

for _ in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    redge[B].append(A)

come = [False] * N
backorder = []
def dfs(x):
    come[x] = True
    for to in edge[x]:
        if come[to]:continue
        dfs(to)
    backorder.append(x)

components = []
def rdfs(x):
    come[x] = True
    components[-1].append(x)
    for to in redge[x]:
        if come[to]:continue
        rdfs(to)



for v in range(N):
    if come[v]:continue
    dfs(v)

backorder.reverse()

come = [False] * N

for v in backorder:
    if come[v]:continue
    components.append([])
    rdfs(v)
ans = 0
for component in components:
    n = len(component)
    ans += n * (n-1) // 2

print(ans)



