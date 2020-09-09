laji = input()
nums = [int(x) for x in input().split()]

ans_lst = [x for x in nums if x != 0]

print(len(ans_lst))
for i in ans_lst:
    print(i, end=' ')