N = int(input())

pare = []
for i in range(1 << N):
    l = ""
    for j in range(N):
        if i >> j & 1:
            l += "("
        else:
            l += ")"

    if len(l) == N:
        cnt = 0
        flag = True
        for k in range(N):
            if l[k] == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                flag = False
                break
        if flag and cnt == 0:
            pare.append(l)

pare.sort()

for i in range(len(pare)):
    print(pare[i])
