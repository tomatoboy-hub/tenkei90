N,B = map(int,input().split())

def f(x):
    ans = 1
    for c in str(x):
        ans += int(c)
    return ans
ans = 0

for two in range(34):
    for three in range(23):
        for five in range(12):
            for seven in range(12):
                fm = 2**two * 3**three * 5**five * 7**seven
                m = fm + B
                if m > N:break
                if f(m) == fm:
                    ans += 1

print(ans)