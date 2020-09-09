class Solution:
    def longestConsecutive(self, nums: list) -> int:
        val_dict = {}
        for i in nums:
            if i not in val_dict:
                val_dict[i] = 1
        ans = 0
        for i in nums:
            tmp = 1
            j = i
            if j -1 not in val_dict:
                while j + 1 in val_dict:
                    j += 1
                    tmp += 1
                ans = max(ans, tmp)
        return ans