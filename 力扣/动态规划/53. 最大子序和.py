class Solution:
    def maxSubArray(self, nums: list) -> int:
        pre = 0
        max_ans = nums[0]
        for i in range(len(nums)):
            pre = max(nums[i], pre+nums[i])
            max_ans = max(max_ans, pre)
        return max_ans

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))