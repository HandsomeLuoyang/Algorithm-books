x = int(input())

ans = 0
mul = 1

for i in range(1, x+1):
    mul *= i
    ans += mul

print(ans)