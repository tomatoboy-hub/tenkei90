N = int(input())
A = list(map(int, input().split()))
dp = [[10**10] * (2 * N+1) for _ in range(2 * N + 1)]

for i in range(N+1):
    dp[i][i] = 0


for width in range(2, 2*N+1 ,2):
    for l in range(2*N):
        r = l + width
        if r > 2*N:break
        for mid in range(l+2,r,2):
            dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid][r])
        dp[l][r] = min(dp[l][r],dp[l+1][r-1] + abs(A[l]-A[r-1]))

print(dp[0][2*N])