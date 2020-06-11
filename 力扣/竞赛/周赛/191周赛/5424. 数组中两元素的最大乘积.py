class Solution:
    def maxProduct(self, nums: list) -> int:
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        return (m1 - 1) * (m2 - 1)