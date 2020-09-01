class Solution:
    def PredictTheWinner(self, nums) -> bool:
        if len(nums) % 2 == 0:
            return True
        self.nums = nums
        return self.helper(0, len(nums)-1, 1) >= 0

    def helper(self, start, end, flag):
        if start == end:
            return self.nums[start] * flag
        score1 = self.helper(start + 1, end, -flag) + self.nums[start] * flag
        score2 = self.helper(start, end - 1, -flag) + self.nums[end] * flag
        return max(score1*flag, score2*flag) * flag
