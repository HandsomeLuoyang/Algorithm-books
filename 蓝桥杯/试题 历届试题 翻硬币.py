base = list(input())
target = list(input())

ans = 0
for i in range(len(base)-1):
    if base[i] != target[i]:
        base[i+1] = '*' if base[i+1] == 'o' else 'o'
        ans += 1


print(ans)
