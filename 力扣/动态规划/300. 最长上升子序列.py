class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append()
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        

s = Solution()
s.lengthOfLIS([1,2,3,4])