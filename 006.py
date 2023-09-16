import string 
import bisect

N,K = map(int,input().split())
S = input()
alphs = list(string.ascii_lowercase)

s_idx = {}

for a in alphs:
    s_idx[a] = []

for i in range(len(S)):
    s_idx[S[i]].append(i)

ans = ""
memo = 0
while K > 0:
    for a in alphs:
        if len(s_idx[a]) == 0:
            continue
        j = bisect.bisect_left(s_idx[a],memo)
        if j > len(s_idx[a]):
            continue
        if K + s_idx[a][j] <= N:
            memo = s_idx[a][j] + 1
            ans += a
            K -= 1
            break

print(ans)
