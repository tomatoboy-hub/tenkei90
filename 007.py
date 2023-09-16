N = int(input())
A = list(map(int,input().split()))
Q = int(input())

A.sort()

ans = []

for i in range(Q):
    b = int(input())
    left = -1
    right = N
    while right - left > 1:
        mid = (left + right)//2
        if A[mid] >= b:
            right = mid
        else:
            left = mid
    
    comp1 = 10 ** 9
    comp2 = 10 ** 9
    if left >= 0:
        comp1 = abs(A[left] - b)
    if left < N-1:
        comp2 = abs(A[left + 1] - b)

    ans.append(min(comp1,comp2))

for a in ans:
    print(a)
