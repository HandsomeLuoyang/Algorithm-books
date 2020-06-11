class Solution:
    def rob(self, nums: list) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length <= 2:
            return max(nums)
        dp = [0 for _ in range(length)]
        dp[0], dp[1] = nums[0], nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]


sol = Solution()
print(sol.rob([2, 1, 1, 2]))
