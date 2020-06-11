class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        hash_dict = {}
        for i in nums:
            if i in hash_dict:
                return i
            else:
                hash_dict[i] = 1