th = int(input())

for num in range(th):
    buyao = input()
    num_1 = [int(x) for x in input().split()]
    num_2 = [int(x) for x in input().split()]

    num_1.sort()
    num_2.sort(reverse=True)

    ans = 0

    for i in range(len(num_1)):
        ans += num_1[i] * num_2[i]

    print(ans)
