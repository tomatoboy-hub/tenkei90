H,W = map(int,input().split())
Q = int(input())

def flatten(h,w):
    return h+(H+1)*W

M = [False] * ((H+1) * W)
n = len(M)

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self,x,y):
        return self.find(x) == self.find(y)
    

uf = UnionFind(n)

for _ in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 1:
        r,c = q[1]-1,q[2]-1
        x = flatten(r,c)
        M[x] = True
        for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
            r_dash,c_dash = r+i,c+j
            y = flatten(r_dash,c_dash)
            if 0 <= r_dash < H and 0 <= c_dash < W:
                if M[y]:
                    uf.union(x,y)
    else:
        x = flatten(q[1]-1,q[2]-1)
        y = flatten(q[3]-1,q[4]-1)
        if M[x] and M[y] and uf.same(x,y):
            print("Yes")
        else:
            print("No")
            