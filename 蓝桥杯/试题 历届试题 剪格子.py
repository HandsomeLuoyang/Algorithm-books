col, row = [int(x) for x in input().split()]

lst = []

for i in range(row):
    lst.append([int(x) for x in input().split()])
_sum = sum(list(map(lambda x: sum(x), lst)))


def dfs(i, j, he, num):
    global _sum
    tmp_sum = he + lst[i][j]
    if tmp_sum == _sum:
        return num
    elif tmp_sum < _sum:
        if i + 1 < row:
            return dfs(i+1, j, tmp_sum, num+1)
        if j + 1 < col:
            return dfs(i, j+1, tmp_sum, num+1)
    else:
        return 100000

print(dfs(0, 0, 0, 0))