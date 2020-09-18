x = int(input())
for i in range(x):
    a, b  = [int(y) for y in input().split()]
    mul = 1
    for j in range(1, a+1):
        mul *= j
    print(str(mul).count(str(b)))