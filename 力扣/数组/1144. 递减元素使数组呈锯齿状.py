class Solution:
    def movesToMakeZigzag(self, nums: list) -> int:
        ans1 = 0 if nums[0] < nums[1] else (nums[0] - nums[1] + 1)
        ans2 = 0
        if (len(nums) - 1) % 2 == 0:
            ans1 += 0 if nums[-1] < nums[-2] else (nums[-1] - nums[-2] + 1)
        else:
            ans2 += 0 if nums[-1] < nums[-2] else (nums[-1] - nums[-2] + 1) 
        for i in range(1, len(nums)-1):
            # 偶数
            if i % 2 == 0:
                ans1 += 0 if nums[i] < min(nums[i-1], nums[i+1]) else (nums[i] - min(nums[i-1], nums[i+1]) + 1)
            else:
                ans2 += 0 if nums[i] < min(nums[i-1], nums[i+1]) else (nums[i] - min(nums[i-1], nums[i+1]) + 1)
        return min(ans1, ans2)

s = Solution()
print(s.movesToMakeZigzag([1,2,3]))