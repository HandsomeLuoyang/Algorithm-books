lst = [int(x) for x in input().split()]

lst.sort(reverse=True)

for i in lst:
    print(i, end=' ')