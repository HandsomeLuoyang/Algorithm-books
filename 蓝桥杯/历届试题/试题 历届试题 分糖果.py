laji = int(input())
nums = [int(x) for x in input().split()]
ans = 0

while len(set(nums)) != 1:
    first_half = 0
    first_half = nums[0] // 2
    nums[0] -= first_half
    for i in range(1, laji):
        nums[i] //= 2
        nums[i-1] += nums[i]
    nums[laji - 1] += first_half

    for i in range(0, laji):
        if nums[i] %2 != 0:
            nums[i] += 1
            ans += 1

print(ans)