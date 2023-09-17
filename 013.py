from heapq import heappush, heappop
N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1; b -= 1
    edge[a].append((b,c))
    edge[b].append((a,c))

def dijkstra(s):
    dist = [10**18]*N
    dist[s] = 0
    pq = [(0,s)]
    while len(pq) != 0:
        d,f = heappop(pq)
        if dist[f] < d:
            continue
        for to,c in edge[f]:
            if dist[to] > dist[f]+c:
                dist[to] = dist[f]+c
                heappush(pq,(dist[to],to))
    return dist

dist0 = dijkstra(0)
distN = dijkstra(N-1)
for i in range(N):
    print(dist0[i]+distN[i])