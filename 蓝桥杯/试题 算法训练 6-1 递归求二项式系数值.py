k, n = [int(x) for x in input().split()]

def helper(k, n):
    if k == 0 or k == n:
        return 1
    return helper(k, n-1) + helper(k-1, n-1)

print(helper(k, n))